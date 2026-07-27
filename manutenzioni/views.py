from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.db.models import Count, Q, Sum

from .forms import InterventoForm
from .models import Intervento, Ricambio, Veicolo
from .serializers import InterventoSerializer, RicambioSerializer, VeicoloSerializer


class VeicoloListView(LoginRequiredMixin, ListView):
    model = Veicolo
    template_name = "manutenzioni/veicolo_list.html"
    context_object_name = "veicoli"
    paginate_by = 6

    def get_queryset(self):
        queryset = Veicolo.objects.filter(proprietario=self.request.user)

        query = self.request.GET.get("q", "").strip()
        sort = self.request.GET.get("sort", "").strip()

        if query:
            queryset = queryset.filter(
                Q(targa__icontains=query) |
                Q(marca__icontains=query) |
                Q(modello__icontains=query)
            )

        allowed_sorts = {
            "marca": "marca",
            "-marca": "-marca",
            "modello": "modello",
            "-modello": "-modello",
            "km_totali": "km_totali",
            "-km_totali": "-km_totali",
            "targa": "targa",
            "-targa": "-targa",
        }

        queryset = queryset.order_by(allowed_sorts.get(sort, "marca"))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_query = self.request.GET.get("q", "").strip()
        sort = self.request.GET.get("sort", "").strip()

        user_vehicles = Veicolo.objects.filter(proprietario=self.request.user)
        user_interventi = Intervento.objects.filter(veicolo__proprietario=self.request.user)

        dashboard = {
            "totale_veicoli": user_vehicles.count(),
            "totale_interventi": user_interventi.count(),
            "costo_totale": user_interventi.aggregate(totale=Sum("costo"))["totale"] or 0,
            "interventi_completati": user_interventi.filter(stato=Intervento.Stato.COMPLETATO).count(),
        }

        context["search_query"] = search_query
        context["sort"] = sort
        context["dashboard"] = dashboard
        return context
class VeicoloDetailView(LoginRequiredMixin, DetailView):
    model = Veicolo
    template_name = "manutenzioni/veicolo_detail.html"
    context_object_name = "veicolo"

    def get_queryset(self):
        return Veicolo.objects.filter(proprietario=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        stato = self.request.GET.get("stato", "").strip()
        data_da = self.request.GET.get("data_da", "").strip()
        data_a = self.request.GET.get("data_a", "").strip()

        interventi = self.object.interventi.all()

        if stato:
            interventi = interventi.filter(stato=stato)

        if data_da:
            interventi = interventi.filter(data__gte=data_da)

        if data_a:
            interventi = interventi.filter(data__lte=data_a)

        metriche = self.object.interventi.aggregate(
            totale_interventi=Count("id"),
            costo_totale=Sum("costo"),
        )

        context["interventi"] = interventi
        context["search_stato"] = stato
        context["search_data_da"] = data_da
        context["search_data_a"] = data_a
        context["metriche"] = metriche

        return context

class InterventoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Intervento
    form_class = InterventoForm
    template_name = "manutenzioni/intervento_form.html"
    success_url = reverse_lazy("manutenzioni:veicolo_list")
    permission_required = "manutenzioni.add_intervento"

    def form_valid(self, form):
        form.instance.meccanico = self.request.user
        return super().form_valid(form)


class VeicoloViewSet(viewsets.ModelViewSet):
    serializer_class = VeicoloSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Veicolo.objects.filter(proprietario=self.request.user)


class InterventoViewSet(viewsets.ModelViewSet):
    serializer_class = InterventoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Intervento.objects.filter(veicolo__proprietario=self.request.user)


class RicambioViewSet(viewsets.ModelViewSet):
    serializer_class = RicambioSerializer
    permission_classes = [IsAuthenticated]
    queryset = Ricambio.objects.all()
class InterventoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Intervento
    form_class = InterventoForm
    template_name = "manutenzioni/intervento_form.html"
    success_url = reverse_lazy("manutenzioni:veicolo_list")
    permission_required = "manutenzioni.add_intervento"

    def form_valid(self, form):
        form.instance.meccanico = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f"Intervento su {form.instance.veicolo} registrato correttamente.")
        return response

    def handle_no_permission(self):
        messages.error(self.request, "Non hai i permessi per creare un intervento.")
        return super().handle_no_permission()