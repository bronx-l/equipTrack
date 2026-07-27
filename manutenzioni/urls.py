from django.urls import path
from django.views.generic import RedirectView

from .views import InterventoCreateView, VeicoloDetailView, VeicoloListView

app_name = "manutenzioni"

urlpatterns = [
    path("", RedirectView.as_view(
            pattern_name="manutenzioni:veicolo_list",
            permanent=False
        ), name="home"),
    path("veicoli/", VeicoloListView.as_view(), name="veicolo_list"),
    path("veicoli/<int:pk>/", VeicoloDetailView.as_view(), name="veicolo_detail"),
    path("interventi/nuovo/", InterventoCreateView.as_view(), name="intervento_create"),
]