from rest_framework import serializers
from .models import *

class EleveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Eleve
        fields = "__all__"

class EnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Enseignant
        fields = "__all__"

class ExerciceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Exercice
        fields = "__all__"

class ImagedockerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Imagedocker
        fields = "__all__"

class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Groupe
        fields = "__all__"

class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Instance
        fields = "__all__"

class RepertoireSerializer(serializers.ModelSerializer):
    class Meta:
        model=Repertoire
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields = "__all__"

class VirtualmachineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Virtualmachine
        fields = "__all__"

class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model=Niveau
        fields = "__all__"

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Score
        fields = "__all__"