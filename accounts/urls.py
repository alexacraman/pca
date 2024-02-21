from django.urls import path
from .views import get_json_team, account_view,login_view , UserUpdateView,CommitteeMembersListView, CommitteeMembersCreateView, CommitteeMembersUpdateView, CommitteeMembersDeleteView, CommitteeMembersDetailView, SignUpView

app_name = 'accounts'

urlpatterns = [
    path('committee-members/', CommitteeMembersListView.as_view(), name='committee-members-list'),
    path('committee-members/create/', CommitteeMembersCreateView.as_view(), name='committee-members-create'),
    path('committee-members/<int:pk>/', CommitteeMembersDetailView.as_view(), name='committee-members-detail'), 
    path('committee-members/<int:pk>/update/', CommitteeMembersUpdateView.as_view(), name='committee-members-update'),
    path('committee-members/<int:pk>/delete/', CommitteeMembersDeleteView.as_view(), name='committee-members-delete'),
    path('get_json_team/', get_json_team, name='get_json_team'),
    # path('custom-login/', login_view, name='custom-login'),
    # Registration (Sign Up)
    path('signup/',SignUpView.as_view(), name='signup'),
    path('profile/', account_view, name='profile'),
    path('login/', login_view, name='login'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(),name='user-update'),

    # # Login
    # path('login/',LoginView.as_view(), name='login'),

    # # Logout
    # path('logout/', LogoutView.as_view(), name='logout'),

    # # Password Change
    # path('password/change/',CustomPasswordChangeView.as_view(), name='password_change'),

    # # Password Reset
    # path('password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),

    # # password reset done
    # path('password/reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),


    # # Password Reset Confirm
    # path('password/reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # # Password Reset Complete
    # path('password/reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    
    
]




