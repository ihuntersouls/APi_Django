from rest_framework.serializers import ModelSerializer
from mainApp.models import Heroe_x_mision

class HeroeMisionSerializer(ModelSerializer):
    class Meta:
        model = Heroe_x_mision
        #fields = '__all__'
        fields = ['id_heroe', 'id_mision', 'estado', 'create_at']