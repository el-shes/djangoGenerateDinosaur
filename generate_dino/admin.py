from django.contrib import admin
from . import models


# Register your models here.


class DinoAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.Dino, DinoAdmin)
admin.site.register(models.GeneratedDino, DinoAdmin)
