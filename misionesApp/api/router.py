from rest_framework.routers import DefaultRouter

from misionesApp.api.views import MisionViewSet

router_mision = DefaultRouter()

router_mision.register(prefix='mision', basename='mision', viewset=MisionViewSet)
