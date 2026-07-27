import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient

from manutenzioni.models import Veicolo


@pytest.mark.django_db
class TestVeicoloAPI:
    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="apiuser", password="testpass123")
        self.other_user = User.objects.create_user(username="otheruser", password="testpass123")

        self.veicolo1 = Veicolo.objects.create(
            targa="API123",
            marca="Fiat",
            modello="Tipo",
            tipo=Veicolo.Tipo.AUTO,
            km_totali=25000,
            proprietario=self.user,
        )
        self.veicolo2 = Veicolo.objects.create(
            targa="API999",
            marca="BMW",
            modello="X1",
            tipo=Veicolo.Tipo.AUTO,
            km_totali=40000,
            proprietario=self.other_user,
        )

    def test_api_requires_authentication(self):
        response = self.client.get("/api/veicoli/")
        assert response.status_code == 403 or response.status_code == 401

    def test_api_returns_only_authenticated_user_vehicles(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/veicoli/")

        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]["targa"] == "API123"
@pytest.mark.django_db
def test_intervento_create_requires_permission(client):
    user = User.objects.create_user(username="meccanico", password="testpass123")
    client.login(username="meccanico", password="testpass123")

    response = client.get(reverse("manutenzioni:intervento_create"))
    assert response.status_code == 403 or response.status_code == 302