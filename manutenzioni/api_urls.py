from rest_framework.routers import DefaultRouter

from .views import InterventoViewSet, RicambioViewSet, VeicoloViewSet

router = DefaultRouter()
router.register(r"veicoli", VeicoloViewSet, basename="veicolo")
router.register(r"interventi", InterventoViewSet, basename="intervento")
router.register(r"ricambi", RicambioViewSet, basename="ricambio")

urlpatterns = router.urls