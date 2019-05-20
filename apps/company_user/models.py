from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from apps.company.models import Company


class CompanyUser(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Name of user",
                            verbose_name="Name:")
    administrator = models.BooleanField(default=False,
                                        help_text="Administrator of System",
                                        verbose_name="Administrator of System")
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True,
                                blank=True)

    def get_absolute_url(self):
        return reverse('company_user_list')

    def __str__(self):
        return self.name
