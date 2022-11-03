from rest_framework.routers import DefaultRouter

from heroesApp.api.views import HeroeViewSet

router_heroe = DefaultRouter()

router_heroe.register(prefix='heroes', basename='heroes', viewset=HeroeViewSet)