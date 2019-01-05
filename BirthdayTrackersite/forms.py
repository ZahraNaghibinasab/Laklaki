from django import forms

from .models import Whole
from .models import Months


class UserForm(forms.ModelForm):

    class Meta:
        model = Whole
        fields = ('day','month')


