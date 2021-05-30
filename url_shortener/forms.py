from .models import URL

from django import forms


class URLForm(forms.ModelForm):
    """Formularz dla modelu URL."""

    original_url = forms.URLField(required=True, label='twój link')

    class Meta:
        model = URL
        fields = ('original_url',)
