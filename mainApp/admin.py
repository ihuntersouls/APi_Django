from django.contrib import admin

from .models import Heroe, Mision, Heroe_x_mision

# admin.site.register(Heroe)
# admin.site.register(Mision)
# admin.site.register(Heroe_x_mision)


@admin.register(Heroe)
class HeroeAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apodo', 'nivel']


@admin.register(Mision)
class MisionAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'lugar', 'create_at']

@admin.register(Heroe_x_mision)
class Heroe_x_mision(admin.ModelAdmin):
    list_display = ['id_heroe', 'id_mision', 'estado', 'create_at']
