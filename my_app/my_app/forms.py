# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import *

# create a ModelForm
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"

class ExerciceForm(forms.ModelForm):
    class Meta:
        model = Exercice
        fields = "__all__"

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = "__all__"

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = "__all__"
