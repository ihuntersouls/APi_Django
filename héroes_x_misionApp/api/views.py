from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from mainApp.models import Heroe_x_mision
from héroes_x_misionApp.api.serializers import HeroeMisionSerializer


class Heroe_X_misionesViewSet(ViewSet):
    def list(self, request):
        heroesmision = HeroeMisionSerializer(Heroe_x_mision.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=heroesmision.data)

    def retrieve(self, request, pk: int):
        Heroemision = HeroeMisionSerializer(Heroe_x_mision.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=Heroemision.data)

    def create(self, request):
        heroemision = HeroeMisionSerializer(data=request.POST)
        heroemision.is_valid(raise_exception=True)
        heroemision.save()
        return Response(status=status.HTTP_200_OK, data=heroemision.data)