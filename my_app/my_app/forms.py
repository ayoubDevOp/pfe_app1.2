# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Message

# create a ModelForm
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"