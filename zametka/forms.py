# zametka/forms.py
from django import forms
from zametka.models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
