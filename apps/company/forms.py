from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Company


class CompanyForm(forms.ModelForm):
    placeholder = _('Center name')
    label = _('Name')
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': placeholder,
                   'label_tag': label
                   }
        )
    )

    class Meta:
        model = Company
        fields = ('name',)
