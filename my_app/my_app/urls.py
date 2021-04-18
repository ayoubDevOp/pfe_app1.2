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
	path('api/', include(router.urls)),
	path('login/', views.login, name = 'login'),
	path('eleve/acueil', views.eleve, name = 'eleve'),
	path('eleve/profile', views.eleve_profile, name = 'eleve_profile'),
	path('eleve/machine', views.eleve_machine, name = 'eleve_machine'),
	path('eleve/mail', views.eleve_mail, name = 'eleve_mail'),
	path('administrator', views.adminstrator, name = 'adminstrator'),
	path('enseignant/acueil', views.enseignant, name = 'enseignant'),
	path('enseignant/exercices', views.enseignant_exercices, name = 'enseignant_exercices'),
	path('enseignant/instances', views.enseignant_instances, name = 'enseignant_instances'),
	path('enseignant/images', views.enseignant_images, name = 'enseignant_images'),
	path('enseignant/supervision', views.enseignant_supervision, name = 'enseignant_supervision'),
	path('enseignant/mail', views.enseignant_mail, name = 'enseignant_mail'),
	path('enseignant/mail_sent', views.enseignant_mail_sent, name = 'enseignant_mail_sent'),
	path('enseignant/mail_compose', views.enseignant_mail_compose, name = 'enseignant_mail_compose'),
	path('', views.login, name='home'),
	path('logout_elv/', views.logout_elv, name='logout_elv'),
	path('logout_ens/', views.logout_ens, name='logout_ens'),
	path('logout_admin/', views.logout_admin, name='logout_admin'),
	path('sign_up_admin/', views.sign_up_admin, name='sign_up_admin'),
	path('sign_up_eleve/', views.sign_up_eleve, name='sign_up_eleve'),
	path('sign_up_ens/', views.sign_up_ens, name='sign_up_ens'),
]
