from django.urls import path
from .views import (
    VenueListView,
    VenueDetailView,
    VenueCreateView,
    VenueUpdateView,
    VenueDeleteView,
)

app_name = 'venue'

urlpatterns = [
    path('', VenueListView.as_view(), name='venue-list'),
    path('<int:pk>/', VenueDetailView.as_view(), name='venue-detail'),
    path('create/', VenueCreateView.as_view(), name='venue-create'),
    path('<int:pk>/update/', VenueUpdateView.as_view(), name='venue-update'),
    path('<int:pk>/delete/', VenueDeleteView.as_view(), name='venue-delete'),
]
