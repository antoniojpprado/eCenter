from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('apps.core.urls')),
    path('panel/', include('apps.panel.urls')),
    path('company/', include('apps.company.urls')),
    path('company_user/', include('apps.company_user.urls')),
)
