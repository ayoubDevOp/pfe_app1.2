from django.contrib import admin
from django.apps import apps

# Register your models here.
from . import *

admin.site.register(models.Eleve)
admin.site.register(models.Enseignant)
admin.site.register(models.Groupe)
#admin.site.register(models.Msg)
admin.site.register(models.Niveau)
admin.site.register(models.Exercice)
admin.site.register(models.Message)
admin.site.register(models.Imagedocker)
admin.site.register(models.Instance)
admin.site.register(models.Repertoire)
admin.site.register(models.Score)
admin.site.register(models.Virtualmachine)