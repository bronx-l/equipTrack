from rest_framework import serializers
from .models import Veicolo, Intervento, Ricambio


class RicambioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ricambio
        fields = ['id', 'nome', 'codice', 'prezzo_unitario']


class InterventoSerializer(serializers.ModelSerializer):
    ricambi_usati = RicambioSerializer(many=True, read_only=True)
    veicolo_targa = serializers.CharField(source='veicolo.targa', read_only=True)
    meccanico_username = serializers.CharField(source='meccanico.username', read_only=True)

    class Meta:
        model = Intervento
        fields = [
            'id',
            'veicolo',
            'veicolo_targa',
            'data',
            'descrizione',
            'km_al_momento',
            'costo',
            'stato',
            'ricambi_usati',
            'meccanico',
            'meccanico_username',
        ]


class VeicoloSerializer(serializers.ModelSerializer):
    interventi = InterventoSerializer(many=True, read_only=True)
    proprietario_username = serializers.CharField(source='proprietario.username', read_only=True)

    class Meta:
        model = Veicolo
        fields = [
            'id',
            'targa',
            'modello',
            'marca',
            'tipo',
            'km_totali',
            'data_immatricolazione',
            'proprietario',
            'proprietario_username',
            'interventi',
        ]