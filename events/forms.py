from .models import Event
from django import forms
 
class CreateEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'end_date','url_link','location', 'cost', 'event_type', 'event_category']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'rounded w-full  my-4 text-gray-600 p-1 outline outline-offset-1 outline-1 focus:outline-none focus:ring focus:ring-blue-400'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'rounded w-full  my-4 text-gray-600 p-1 outline outline-offset-1 outline-1 focus:outline-none focus:ring focus:ring-blue-400'}
            ),
            'start_date': forms.DateInput(
                attrs={'type': 'datetime-local', 'class': 'rounded w-full  my-4 text-gray-600 p-1 outline outline-offset-1 outline-1 focus:outline-none focus:ring focus:ring-blue-400'},
                format='%Y-%m-%dT%H:%M'
            ),
            'end_date': forms.DateInput(
                attrs={'type': 'datetime-local', 'class': 'rounded w-full  my-4 text-gray-600 p-1 outline outline-offset-1 outline-1 focus:outline-none focus:ring focus:ring-blue-400'},
                format='%Y-%m-%dT%H:%M'
            ),
            'cost': forms.NumberInput(
                attrs={'class': 'rounded w-full  my-4 text-gray-600 p-1 outline outline-offset-1 outline-1 focus:outline-none focus:ring focus:ring-blue-400'}
            ),
            'location': forms.TextInput(
                attrs={'class': 'rounded w-full  my-4 text-gray-600 p-1 outline outline-offset-1 outline-1 focus:outline-none focus:ring focus:ring-blue-400'}
            ),
            'url_link': forms.URLInput(
                attrs={'class': 'rounded w-full  my-4 text-gray-600 p-1 outline outline-offset-1 outline-1 focus:outline-none focus:ring focus:ring-blue-400'}
            ),
            'event_type':forms.TextInput(
                attrs={'class': 'rounded w-full  my-4 text-gray-600 p-1 outline outline-offset-1 outline-1 focus:outline-none focus:ring focus:ring-blue-400'}
            ),
            'event_category': forms.TextInput(
                attrs={'class': 'rounded w-full  my-4 text-gray-600 p-1 outline outline-offset-1 outline-1 focus:outline-none focus:ring focus:ring-blue-400'}
            ),
            
        }