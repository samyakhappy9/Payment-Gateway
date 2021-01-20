  
from django import forms

class DonateForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    number = forms.IntegerField()
    amount = forms.IntegerField()