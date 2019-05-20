from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def PanelView(request):
    return render(request, 'panel_form.html')
