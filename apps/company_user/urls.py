from django.urls import path
from .views import (
    CompanyUserList,
    CompanyUserEdit,
    CompanyUserDelete,
    CompanyUserNew
)

urlpatterns = [
    path('company_user_list/', CompanyUserList.as_view(),
         name='company_user_list'),
    path('company_user_new/', CompanyUserNew.as_view(),
         name='company_user_new'),
    path('company_user_edit/<int:pk>/', CompanyUserEdit.as_view(),
         name='company_user_edit'),
    path('company_user_delete/<int:pk>/', CompanyUserDelete.as_view(),
         name='company_user_delete'),
]
