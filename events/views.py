from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Event
from .forms import CreateEvent

class CreateEvent(LoginRequiredMixin, CreateView):
    model           = Event
    template_name   = 'events/create_event.html'
    form_class      = CreateEvent
    success_url     = reverse_lazy('events:event-list')
    ordering        = 'created'

class EventList(ListView):
    model               = Event
    template_name       = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by         = 8

    def get_queryset(self):
        queryset = super().get_queryset().order_by('created')
        return queryset

class EventDetail(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'events/event_detail.html'

    def get_object(self, queryset=None):
        event = super().get_object(queryset=queryset)
        event.views += 1
        event.save()  
        return event
    
class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'events/event_delete.html'
    success_url = reverse_lazy('events:event-list')


class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = 'events/event_update.html'
    fields = ['title', 'description', 'start_date', 'end_date', 'location', 'image', 'url_link', 'cost', 'event_type', 'event_category', 'is_featured']

    
# events/views.py
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Event
# from .forms import AttendeeForm

# def event_detail(request, event_id):
#     event = get_object_or_404(Event, pk=event_id)

#     # Increment the views count
#     event.views += 1
#     event.save()

#     if request.method == 'POST':
#         form = AttendeeForm(request.POST)
#         if form.is_valid():
#             attendee = form.save(commit=False)
#             attendee.event = event
#             attendee.save()
#             return redirect('event_detail', event_id=event_id)
#     else:
#         form = AttendeeForm()

#     return render(request, 'events/event_detail.html', {'event': event, 'form': form})

