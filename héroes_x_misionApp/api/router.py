from rest_framework.routers import DefaultRouter

from héroes_x_misionApp.api.views import Heroe_X_misionesViewSet

router_heroemision = DefaultRouter()

router_heroemision.register(
    prefix='heroes', basename='heroes', viewset=Heroe_X_misionesViewSet)
