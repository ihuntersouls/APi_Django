from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from mainApp.models import Heroe
from heroesApp.api.selializers import HeroeSerializer


class HeroeViewSet(ViewSet):
    def list(self, request):
        heroes = HeroeSerializer(Heroe.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=heroes.data)
    
    def retrieve(self, request, pk: int):
        heroe = HeroeSerializer(Heroe.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=heroe.data)
    
    def create(self, request):
        heroe = HeroeSerializer(data=request.POST)
        heroe.is_valid(raise_exception=True)
        heroe.save()
        return Response(status=status.HTTP_200_OK, data=heroe.data)

