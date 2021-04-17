"""my_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from my_app import views

router = routers.DefaultRouter()

router.register('eleves', views.EleveAPI)
router.register('enseignant', views.EnseignantAPI)
router.register('groupes', views.GroupeAPI)
router.register('messages', views.MessageAPI)
router.register('niveaus', views.NiveauAPI)
router.register('exercices', views.ExerciceAPI)
router.register('imagedockers', views.ImagedockerAPI)
router.register('instances', views.InstanceAPI)
router.register('repertoires', views.RepertoireAPI)
router.register('virtualmachines', views.VirtualmachineAPI)
router.register('scores', views.ScoreAPI)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),]
