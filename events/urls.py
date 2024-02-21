from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('create/', views.CreateEvent.as_view(), name='create-event'),
    path('events/', views.EventList.as_view(), name='event-list'),
    path('event/<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('event/<int:pk>/delete/', views.EventDelete.as_view(), name='event-delete'),
    path('event/<int:pk>/update/', views.EventUpdate.as_view(), name='event-update'),
]