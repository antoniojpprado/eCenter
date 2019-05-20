from django.urls import path
from .views import PanelView


urlpatterns = [
    path('', PanelView, name='panel_view'),
]
