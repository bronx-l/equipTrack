from django import forms
from .models import Intervento


class InterventoForm(forms.ModelForm):
    class Meta:
        model = Intervento
        fields = ["veicolo", "data", "descrizione", "km_al_momento", "costo", "stato", "ricambi_usati"]
        widgets = {
            "data": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "descrizione": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "veicolo": forms.Select(attrs={"class": "form-select"}),
            "km_al_momento": forms.NumberInput(attrs={"class": "form-control"}),
            "costo": forms.NumberInput(attrs={"class": "form-control"}),
            "stato": forms.Select(attrs={"class": "form-select"}),
            "ricambi_usati": forms.SelectMultiple(attrs={"class": "form-select"}),
        }

    def clean_costo(self):
        costo = self.cleaned_data["costo"]
        if costo < 0:
            raise forms.ValidationError("Il costo non può essere negativo.")
        return costo