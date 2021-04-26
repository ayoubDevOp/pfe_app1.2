# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import *

# create a ModelForm
class MessageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = "__all__"
	"""subject = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "Sujet",
				"class": "form-control"
			}
		))

	content = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "content",
				"class": "form-control"
			}
		))"""



class ExerciceForm(forms.ModelForm):
	
	desig_ex = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "Designation",
				"class": "form-control"
			}
		))


	descr_ex = forms.CharField(
		widget=forms.Textarea(
			attrs={
				"placeholder": "Desctription",
				"class": "form-control"
			}
		))

	lien = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "Lien",
				"class": "form-control"
			}
		))
	
	json_file = forms.CharField(
		widget=forms.Textarea(
			attrs={
				"placeholder": "Json",
				"class": "form-control"
			}
		))

	but = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "but de TP",
				"class": "form-control"
			}
		))

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
