from django import forms

from .models import Whole

class UserForm(forms.ModelForm):

    class Meta:
        model = Whole
        fields = ('day','month')

