from django.shortcuts import render
from django.utils import translation
from django.contrib.auth.decorators import login_required
from apps.company_user.models import CompanyUser


@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/index.html', data)


@login_required
def home_en(request):
    data = {}
    data['usuario'] = request.user
    translation.activate("en")
    return render(request, 'core/index.html', data)


@login_required
def home_pt(request):
    data = {}
    data['usuario'] = request.user
    translation.activate("pt")
    return render(request, 'core/index.html', data)
