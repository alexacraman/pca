from django.urls import path
from .views import (
    MembershipListView,
    MembershipDetailView,
    MembershipCreateView,
    MembershipUpdateView,
    MembershipDeleteView,

)
app_name= 'membership'

urlpatterns = [
    path('memberships/', MembershipListView.as_view(), name='membership-list'),
    path('memberships/<int:pk>/', MembershipDetailView.as_view(), name='membership-detail'),
    path('memberships/create/', MembershipCreateView.as_view(), name='membership-create'),
    path('memberships/<int:pk>/update/', MembershipUpdateView.as_view(), name='membership-update'),
    path('memberships/<int:pk>/delete/', MembershipDeleteView.as_view(), name='membership-delete'),
]