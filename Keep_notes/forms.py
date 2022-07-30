from django.forms import ModelForm
from . models import notes_storage


class Notes_form(ModelForm):
    class Meta:
        model=notes_storage
        fields='__all__'
