from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from mainApp.models import Mision
from misionesApp.api.serializers import MisionSerializer


class MisionViewSet(ViewSet):
    def list(self, request):
        misiones = MisionSerializer(Mision.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=misiones.data)
    
    def retrieve(self, request, pk: int):
        mision = MisionSerializer(Mision.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=mision.data)
    
    def create(self, request):
        mision = MisionSerializer(data=request.POST)
        mision.is_valid(raise_exception=True)
        mision.save()
        return Response(status=status.HTTP_200_OK, data=mision.data)


