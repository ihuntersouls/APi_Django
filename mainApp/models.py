from django.db import models


class Heroe(models.Model):
    nombre = models.CharField(max_length=255)
    nivel = models.IntegerField()
    apodo = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.apodo


class Mision(models.Model):
    descripcion = models.CharField(max_length=255)
    lugar = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.descripcion


class Heroe_x_mision(models.Model):
    id_heroe = models.ForeignKey(Heroe, on_delete=models.CASCADE)
    id_mision = models.ForeignKey(Mision, on_delete=models.CASCADE)
    estado = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.estado
