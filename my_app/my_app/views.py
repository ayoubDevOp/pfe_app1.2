from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class EleveAPI(viewsets.ModelViewSet):
    serializer_class = EleveSerializer
    queryset = Eleve.objects.all()

class EnseignantAPI(viewsets.ModelViewSet):
    serializer_class = EnseignantSerializer
    queryset = Enseignant.objects.all()

class ExerciceAPI(viewsets.ModelViewSet):
    serializer_class = ExerciceSerializer
    queryset = Exercice.objects.all()

class ImagedockerAPI(viewsets.ModelViewSet):
    serializer_class = ImagedockerSerializer
    queryset = Imagedocker.objects.all()

class InstanceAPI(viewsets.ModelViewSet):
    serializer_class = InstanceSerializer
    queryset = Instance.objects.all()

class RepertoireAPI(viewsets.ModelViewSet):
    serializer_class = RepertoireSerializer
    queryset = Repertoire.objects.all()

class VirtualmachineAPI(viewsets.ModelViewSet):
    serializer_class = VirtualmachineSerializer
    queryset = Virtualmachine.objects.all()

class GroupeAPI(viewsets.ModelViewSet):
    serializer_class = GroupeSerializer
    queryset = Groupe.objects.all()

class MessageAPI(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class NiveauAPI(viewsets.ModelViewSet):
    serializer_class = NiveauSerializer
    queryset = Niveau.objects.all()

class ScoreAPI(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()