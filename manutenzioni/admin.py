from django.contrib import admin

from .models import Intervento, Ricambio, Veicolo


@admin.register(Veicolo)
class VeicoloAdmin(admin.ModelAdmin):
    list_display = ("targa", "marca", "modello", "tipo", "km_totali", "proprietario", "costo_totale_manutenzioni")
    list_filter = ("tipo",)
    search_fields = ("targa", "marca", "modello")
    list_editable = ("km_totali",)
    readonly_fields = ("creato_il",)

    fieldsets = (
        ("Identificazione veicolo", {"fields": ("targa", "marca", "modello", "tipo")}),
        ("Dati tecnici", {"fields": ("km_totali", "data_immatricolazione")}),
        ("Proprietario", {"fields": ("proprietario",)}),
        ("Metadati", {"fields": ("creato_il",), "classes": ("collapse",)}),
    )

    def costo_totale_manutenzioni(self, obj):
        return f"€ {obj.costo_totale_manutenzioni:.2f}"
    costo_totale_manutenzioni.short_description = "Costo totale"


@admin.register(Ricambio)
class RicambioAdmin(admin.ModelAdmin):
    list_display = ("nome", "codice", "prezzo_unitario")
    search_fields = ("nome", "codice")


@admin.register(Intervento)
class InterventoAdmin(admin.ModelAdmin):
    list_display = ("veicolo", "data", "stato", "costo", "meccanico")
    list_filter = ("stato", "data")
    search_fields = ("veicolo__targa", "descrizione")
    date_hierarchy = "data"
    filter_horizontal = ("ricambi_usati",)

    fieldsets = (
        ("Intervento", {"fields": ("veicolo", "data", "stato", "descrizione")}),
        ("Dettagli tecnici", {"fields": ("km_al_momento", "costo", "ricambi_usati")}),
        ("Responsabile", {"fields": ("meccanico",)}),
    )