from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(
        max_length=200,
        help_text=_('Company name'),
        verbose_name=_('Name'),
    )

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name
