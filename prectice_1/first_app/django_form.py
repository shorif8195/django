from django import forms

class Django_form(forms.Form):
        name = forms.CharField()
        email = forms.EmailField()
        