from django.contrib.auth.models import User
from django.db import models


class Veicolo(models.Model):
    class Tipo(models.TextChoices):
        AUTO = "auto", "Automobile"
        AGRICOLO = "agricolo", "Macchina agricola"
        CAMPER = "camper", "Camper"

    targa = models.CharField(max_length=10, unique=True)
    modello = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=Tipo.choices, default=Tipo.AUTO)
    km_totali = models.PositiveIntegerField(default=0)
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="veicoli")
    data_immatricolazione = models.DateField(null=True, blank=True)
    creato_il = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["marca", "modello", "targa"]
        verbose_name = "Veicolo"
        verbose_name_plural = "Veicoli"

    def __str__(self):
        return f"{self.marca} {self.modello} ({self.targa})"

    @property
    def costo_totale_manutenzioni(self):
        return sum(intervento.costo for intervento in self.interventi.all())


class Ricambio(models.Model):
    nome = models.CharField(max_length=100)
    codice = models.CharField(max_length=50, unique=True)
    prezzo_unitario = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Ricambio"
        verbose_name_plural = "Ricambi"

    def __str__(self):
        return f"{self.nome} ({self.codice})"


class Intervento(models.Model):
    class Stato(models.TextChoices):
        PROGRAMMATO = "programmato", "Programmato"
        IN_CORSO = "in_corso", "In corso"
        COMPLETATO = "completato", "Completato"

    veicolo = models.ForeignKey(Veicolo, on_delete=models.CASCADE, related_name="interventi")
    data = models.DateField()
    descrizione = models.TextField()
    km_al_momento = models.PositiveIntegerField()
    costo = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    stato = models.CharField(max_length=20, choices=Stato.choices, default=Stato.PROGRAMMATO)
    ricambi_usati = models.ManyToManyField(Ricambio, blank=True, related_name="interventi")
    meccanico = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="interventi_eseguiti",
    )

    class Meta:
        ordering = ["-data"]
        verbose_name = "Intervento"
        verbose_name_plural = "Interventi"

    def __str__(self):
        return f"{self.veicolo} - {self.data} - {self.get_stato_display()}"