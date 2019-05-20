from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import CompanyUser


class CompanyUserList(ListView):
    model = CompanyUser

    def get_queryset(self):
        company_logged = self.request.user.companyuser.company
        return CompanyUser.objects.filter(company=company_logged)


class CompanyUserEdit(UpdateView):
    model = CompanyUser
    fields = ['name', 'administrator']


class CompanyUserDelete(DeleteView):
    model = CompanyUser
    success_url = reverse_lazy('company_user_list')


class CompanyUserNew(CreateView):
    model = CompanyUser
    fields = ['name', 'administrator']

    def form_valid(self, form):
        company_user = form.save(commit=False)
        username = company_user.name.split(' ')[0] + \
                   company_user.name.split(' ')[1]
        company_user.company = self.request.user.companyuser.company
        company_user.user = User.objects.create(username=username)
        company_user.save()
        return super(CompanyUserNew, self).form_valid(form)
