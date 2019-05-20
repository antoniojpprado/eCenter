from django import forms


class PanelForm(forms.Form):
    name = forms.CharField()
