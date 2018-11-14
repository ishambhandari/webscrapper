from django import forms
from django.db import models
from .models import Note

class NoteModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title','content','image']
