import pytest
from django.contrib.auth.models import User

from manutenzioni.models import Intervento, Ricambio, Veicolo


@pytest.mark.django_db
class TestVeicoloModel:
    def setup_method(self):
        self.user = User.objects.create_user(username="mario", password="testpass123")
        self.veicolo = Veicolo.objects.create(
            targa="AB123CD",
            marca="Fiat",
            modello="Panda",
            tipo=Veicolo.Tipo.AUTO,
            km_totali=50000,
            proprietario=self.user,
        )

    def test_str_representation(self):
        assert str(self.veicolo) == "Fiat Panda (AB123CD)"

    def test_default_km_totali(self):
        nuovo = Veicolo.objects.create(
            targa="ZZ999ZZ",
            marca="Ford",
            modello="Focus",
            tipo=Veicolo.Tipo.AUTO,
            proprietario=self.user,
        )
        assert nuovo.km_totali == 0


@pytest.mark.django_db
class TestRicambioModel:
    def test_str_representation(self):
        ricambio = Ricambio.objects.create(
            nome="Filtro olio",
            codice="FO123",
            prezzo_unitario=19.90,
        )
        assert str(ricambio) == "Filtro olio (FO123)"


@pytest.mark.django_db
class TestInterventoModel:
    def setup_method(self):
        self.user = User.objects.create_user(username="meccanico", password="testpass123")
        self.owner = User.objects.create_user(username="owner", password="testpass123")
        self.veicolo = Veicolo.objects.create(
            targa="INT123",
            marca="Iveco",
            modello="Daily",
            tipo=Veicolo.Tipo.CAMPER,
            proprietario=self.owner,
        )

    def test_str_representation(self):
        intervento = Intervento.objects.create(
            veicolo=self.veicolo,
            data="2026-07-27",
            descrizione="Tagliando completo",
            km_al_momento=45000,
            costo=250,
            stato=Intervento.Stato.COMPLETATO,
            meccanico=self.user,
        )
        assert "Iveco Daily (INT123)" in str(intervento)
        assert "Completato" in str(intervento)

    def test_costo_totale_manutenzioni_property(self):
        Intervento.objects.create(
            veicolo=self.veicolo,
            data="2026-07-01",
            descrizione="Cambio olio",
            km_al_momento=40000,
            costo=100,
            stato=Intervento.Stato.COMPLETATO,
        )
        Intervento.objects.create(
            veicolo=self.veicolo,
            data="2026-07-15",
            descrizione="Cambio filtro",
            km_al_momento=42000,
            costo=50,
            stato=Intervento.Stato.COMPLETATO,
        )

        assert self.veicolo.costo_totale_manutenzioni == 150