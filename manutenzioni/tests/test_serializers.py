import pytest
from django.contrib.auth.models import User

from manutenzioni.models import Intervento, Ricambio, Veicolo
from manutenzioni.serializers import InterventoSerializer, RicambioSerializer, VeicoloSerializer


@pytest.mark.django_db
class TestRicambioSerializer:
    def test_serializer_fields(self):
        ricambio = Ricambio.objects.create(
            nome="Pastiglie freno",
            codice="PF001",
            prezzo_unitario=79.90,
        )

        data = RicambioSerializer(ricambio).data

        assert data["nome"] == "Pastiglie freno"
        assert data["codice"] == "PF001"


@pytest.mark.django_db
class TestInterventoSerializer:
    def setup_method(self):
        self.owner = User.objects.create_user(username="owner", password="testpass123")
        self.meccanico = User.objects.create_user(username="meccanico", password="testpass123")
        self.veicolo = Veicolo.objects.create(
            targa="DRF123",
            marca="Fiat",
            modello="Ducato",
            tipo=Veicolo.Tipo.CAMPER,
            proprietario=self.owner,
        )
        self.ricambio = Ricambio.objects.create(
            nome="Filtro aria",
            codice="FA001",
            prezzo_unitario=35.50,
        )

    def test_intervento_serializer_includes_related_fields(self):
        intervento = Intervento.objects.create(
            veicolo=self.veicolo,
            data="2026-07-20",
            descrizione="Manutenzione ordinaria",
            km_al_momento=30000,
            costo=120,
            stato=Intervento.Stato.COMPLETATO,
            meccanico=self.meccanico,
        )
        intervento.ricambi_usati.add(self.ricambio)

        data = InterventoSerializer(intervento).data

        assert data["veicolo_targa"] == "DRF123"
        assert data["meccanico_username"] == "meccanico"
        assert len(data["ricambi_usati"]) == 1
        assert data["ricambi_usati"][0]["codice"] == "FA001"


@pytest.mark.django_db
class TestVeicoloSerializer:
    def setup_method(self):
        self.owner = User.objects.create_user(username="owner2", password="testpass123")
        self.meccanico = User.objects.create_user(username="meccanico2", password="testpass123")
        self.veicolo = Veicolo.objects.create(
            targa="VEI456",
            marca="Ford",
            modello="Transit",
            tipo=Veicolo.Tipo.CAMPER,
            proprietario=self.owner,
        )

    def test_veicolo_serializer_includes_nested_interventi(self):
        Intervento.objects.create(
            veicolo=self.veicolo,
            data="2026-07-10",
            descrizione="Revisione",
            km_al_momento=12000,
            costo=200,
            stato=Intervento.Stato.PROGRAMMATO,
            meccanico=self.meccanico,
        )

        data = VeicoloSerializer(self.veicolo).data

        assert data["targa"] == "VEI456"
        assert data["proprietario_username"] == "owner2"
        assert len(data["interventi"]) == 1
        assert data["interventi"][0]["descrizione"] == "Revisione"