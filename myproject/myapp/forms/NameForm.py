from django import forms


class NameForm(forms.Form):
    name = forms.CharField(label='Name is', max_length=100)
