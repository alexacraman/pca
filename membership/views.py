from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .models import Membership, Address, MembershipInterest
from django.contrib import messages
from .forms import InterestForm, Addressform


class MembershipListView(ListView):
    model = Membership
    template_name = 'membership/membership_list.html'  
    context_object_name = 'memberships'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['interests'] = MembershipInterest.objects.all()
        return context

class MembershipDetailView(DetailView):
    model = Membership
    template_name = 'membership/membership_detail.html'  
    context_object_name = 'membership'

class MembershipCreateView(CreateView):
    model = MembershipInterest
    form_class = InterestForm
    template_name = 'membership/membership_form.html' 

    def get_success_url(self) -> str:
        success_url = reverse_lazy('membership:membership-list')
        return success_url
    
    # fields = ['title', 'first_name', 'last_name', 'place_of_work_study', 'job_title', 'work_address', 'email', 'qualification_status', 'qualification', 'qualification_location', 'year_of_qualification', 'other_qualifications', 'data_use_permission']

class MembershipUpdateView(UpdateView):
    model = MembershipInterest
    template_name = 'membership/membership_form.html'
    fields = ['title', 'first_name', 'last_name', 'place_of_work_study', 'job_title', 'work_address', 'email', 'qualification_status', 'qualification', 'qualification_location', 'year_of_qualification', 'other_qualifications', 'data_use_permission']

class MembershipDeleteView(DeleteView):
    model = Membership
    template_name = 'membership/membership_confirm_delete.html'  
    success_url = reverse_lazy('membership:membership-list')  





