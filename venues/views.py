from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Venue

class VenueListView(ListView):
    model = Venue
    template_name = 'venue/venue_list.html'
    context_object_name = 'venues'

class VenueDetailView(DetailView):
    model = Venue
    template_name = 'venue/venue_detail.html'
    context_object_name = 'venue'

class VenueCreateView(LoginRequiredMixin, CreateView):
    model = Venue
    template_name = 'venue/venue_form.html'
    fields = ['name', 'address', 'description', 'phone', 'email', 'website', 'latitude', 'longitude']
    success_url = reverse_lazy('venues:venue-list')

class VenueUpdateView(LoginRequiredMixin, UpdateView):
    model = Venue
    template_name = 'venue/venue_form.html'
    fields = ['name', 'address', 'description', 'phone', 'email', 'website', 'latitude', 'longitude']
    context_object_name = 'venue'
    success_url = reverse_lazy('venues:venue-list')

class VenueDeleteView(LoginRequiredMixin, DeleteView):
    model = Venue
    template_name = 'venue/venue_confirm_delete.html'
    context_object_name = 'venue'
    success_url = reverse_lazy('venues:venue-list')

