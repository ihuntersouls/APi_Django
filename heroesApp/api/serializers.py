
from rest_framework.serializers import ModelSerializer
from mainApp.models import Heroe

class HeroeSerializer(ModelSerializer):
    class Meta:
        model = Heroe
        #fields = '__all__'
        fields = ['id', 'nombre', 'nivel', 'apodo']