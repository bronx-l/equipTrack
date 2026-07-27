import pytest
from django.contrib.auth.models import Permission, User
from django.urls import reverse

from manutenzioni.models import Intervento, Veicolo


@pytest.mark.django_db
class TestVeicoloViews:
    def setup_method(self):
        self.user = User.objects.create_user(username="mario", password="testpass123")
        self.other_user = User.objects.create_user(username="luigi", password="testpass123")

        self.veicolo1 = Veicolo.objects.create(
            targa="AB123CD",
            marca="Fiat",
            modello="Panda",
            tipo=Veicolo.Tipo.AUTO,
            km_totali=50000,
            proprietario=self.user,
        )
        self.veicolo2 = Veicolo.objects.create(
            targa="EF456GH",
            marca="Ford",
            modello="Focus",
            tipo=Veicolo.Tipo.AUTO,
            km_totali=80000,
            proprietario=self.user,
        )
        self.veicolo3 = Veicolo.objects.create(
            targa="ZZ999ZZ",
            marca="Tesla",
            modello="Model 3",
            tipo=Veicolo.Tipo.AUTO,
            km_totali=10000,
            proprietario=self.other_user,
        )

    def test_vehicle_list_requires_login(self, client):
        response = client.get(reverse("manutenzioni:veicolo_list"))
        assert response.status_code == 302

    def test_vehicle_list_shows_only_user_vehicles(self, client):
        client.login(username="mario", password="testpass123")
        response = client.get(reverse("manutenzioni:veicolo_list"))

        assert response.status_code == 200
        veicoli = response.context["veicoli"]
        assert self.veicolo1 in veicoli
        assert self.veicolo2 in veicoli
        assert self.veicolo3 not in veicoli

    def test_vehicle_search_filters_results(self, client):
        client.login(username="mario", password="testpass123")
        response = client.get(reverse("manutenzioni:veicolo_list"), {"q": "Fiat"})

        veicoli = response.context["veicoli"]
        assert self.veicolo1 in veicoli
        assert self.veicolo2 not in veicoli

    def test_vehicle_sorting_by_km_desc(self, client):
        client.login(username="mario", password="testpass123")
        response = client.get(reverse("manutenzioni:veicolo_list"), {"sort": "-km_totali"})

        veicoli = list(response.context["veicoli"])
        assert veicoli[0] == self.veicolo2
        assert veicoli[1] == self.veicolo1
@pytest.mark.django_db
class TestVeicoloPagination:
    def setup_method(self):
        self.user = User.objects.create_user(username="anna", password="testpass123")

        for i in range(8):
            Veicolo.objects.create(
                targa=f"TEST{i}",
                marca="Marca",
                modello=f"Modello{i}",
                tipo=Veicolo.Tipo.AUTO,
                km_totali=1000 * i,
                proprietario=self.user,
            )

    def test_vehicle_list_is_paginated(self, client):
        client.login(username="anna", password="testpass123")
        response = client.get(reverse("manutenzioni:veicolo_list"))

        assert response.status_code == 200
        assert response.context["is_paginated"] is True
        assert len(response.context["veicoli"]) == 6