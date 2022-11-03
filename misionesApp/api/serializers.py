from rest_framework.serializers import ModelSerializer
from mainApp.models import Mision

class MisionSerializer(ModelSerializer):
    class Meta:
        model = Mision
        #fields = '__all__'
        fields = ['descripcion', 'lugar', 'create_at']