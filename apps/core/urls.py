from django.urls import path
from .views import home, home_en, home_pt


urlpatterns = [
    path('', home, name='home'),
    path('en', home_en, name='home_en'),
    path('pt', home_pt, name='home_pt'),
]
