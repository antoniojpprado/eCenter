from django.urls import path
from .views import CompanyEdit


urlpatterns = [
    path('edit/<int:id>/', CompanyEdit, name='company_edit'),
]
