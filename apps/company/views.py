from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import CompanyForm


@login_required
def CompanyEdit(request, id):
    company = get_object_or_404(Company, pk=id)
    form = CompanyForm(request.POST or None, request.FILES or None, instance=company)

    if form.is_valid():
        form.save()

    return render(request, 'company_form.html', {'form': form})
