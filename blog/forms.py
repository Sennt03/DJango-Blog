from django import forms
from django.forms import ModelForm
from .models import Article

class FormCategory(forms.Form):

    name = forms.CharField(
        label = 'Nombre'
    )


class FormEntry(ModelForm):

    class Meta:
        model = Article
        fields = '__all__'