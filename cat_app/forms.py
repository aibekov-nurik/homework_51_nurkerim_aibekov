# cat_app/forms.py
from django import forms
from .models import Cat

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name']

class ActionForm(forms.Form):
    ACTIONS = [
        ('feed', 'Feed'),
        ('play', 'Play'),
        ('sleep', 'Sleep'),
    ]
    action = forms.ChoiceField(choices=ACTIONS)
