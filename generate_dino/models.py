from django.db import models


# Create your models here.

class Dino(models.Model):
    name = models.CharField(max_length=200)

    @classmethod
    def create(cls, name):
        dino = cls(name=name)
        return dino


class GeneratedDino(models.Model):
    name = models.CharField(max_length=200)
