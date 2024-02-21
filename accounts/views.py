import json
from django.core.mail import BadHeaderError, EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login
# from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from accounts.models import CommitteeMembers
from events.models import Event
from venues.models import Venue
from pdf.models import PDFDocument
from membership.models import MembershipInterest
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from .models import CommitteeMembers, CustomUser
from .forms import CommitteeMembersForm, CustomUserCreationFormEmail, CustomUserLoginForm



class SignUpView(CreateView):
    form_class = CustomUserCreationFormEmail
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.is_approved = False
        user_email = form.instance.email
        response =  super().form_valid(form)
        text_content = "Thank you very much for registering for the website. Once approved, you will be notified"
        html_content = """
        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Registration Confirmation</title>
                <style>
                    body{
                        padding:1rem;
                    }
                    table {
                        border-collapse: collapse;
                        width: 100%;
                    }
                    th, td {
                        border: 1px solid #dddddd;
                        text-align: left;
                        padding: 8px;
                    }
                    th {
                        background-color: #f2f2f2;
                    }
                </style>
            </head>
            <body>
                <table>
                    <tr>
                        <th colspan="2">Registration Confirmation</th>
                    </tr>
                    <tr>
                        <td colspan="2">Dear Sir/Madam,</td>
                    </tr>
                    <tr>
                        <td colspan="2">Thank you for registering to use the site. We will email you once approved in order for you to be able to login.</td>
                    </tr>
                    <tr>
                        <td colspan="2">Kind Regards</td>
                    </tr>
                </table>
            </body>
            </html>
        """
        try:
            emailMessage = EmailMultiAlternatives(
                subject      = f"New User Request - PCA",
                body         = text_content,
                from_email   = settings.DEFAULT_FROM_EMAIL,
                to           = [user_email],
                reply_to     = [settings.DEFAULT_FROM_EMAIL]
                )    
            emailMessage.attach_alternative(html_content, "text/html")
            emailMessage.send(fail_silently=False)
        except BadHeaderError as e:
            raise ValueError(e)
        except Exception as e:
            print(f'There was an error: {str(e)}')  
        return response    



def login_view(request):
    form = CustomUserLoginForm()
    if request.method == "POST":
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                custom_user = CustomUser.objects.get(email=email)
                if custom_user.is_approved:
                 
                    login(request, user)
                    return redirect('accounts:profile')
                else:
                    messages.info(request, 'Your account is not approved yet.')
            else:
                messages.info(request, 'Invalid email or password.')
    return render(request, 'registration/login.html', {'form': form})

            

    

@login_required
def account_view(request):
    interests   = MembershipInterest.objects.all()
    members     = CommitteeMembers.objects.all()
    events      = Event.objects.all().order_by('-created')
    venues      = Venue.objects.all()
    pdfs        = PDFDocument.objects.all()
    users       = CustomUser.objects.all()
    now         = timezone.now()
    context = {
        'interests': interests,
        'members': members,
        'events': events,
        'venues': venues,
        'pdfs': pdfs,
        'users': users,
        'now': now,
    }
    return render(request, 'registration/dashboard.html', context)





class UserListView(ListView):
    model = CustomUser
    template_name = 'users/user_list.html' 
    context_object_name = 'users'

class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'users/user_profile.html' 
    context_object_name = 'user'

from django.contrib.auth.mixins import UserPassesTestMixin
class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = CustomUser 
    fields = ['is_approved']  

    def test_func(self):
        return self.request.user.is_superuser 

    def post(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        user = CustomUser.objects.get(pk=user_id)
        user.is_approved = not user.is_approved  # Toggle approval status
        user.save()
        response_data = {
            'success': True,
            'user_id': user.id,
            'is_approved': user.is_approved
        }
        return JsonResponse(response_data)


class CommitteeMembersDetailView(DetailView):
    model = CommitteeMembers
    template_name = 'committee_members/detail.html'
    context_object_name = 'committee_member'


class CommitteeMembersListView(ListView):
    model = CommitteeMembers
    template_name = 'committee_members/list.html'
    context_object_name = 'committee_members'

class CommitteeMembersCreateView(CreateView):
    model = CommitteeMembers
    template_name = 'committee_members/form.html'
    form_class = CommitteeMembersForm
    success_url = reverse_lazy('accounts:committee-members-list')

class CommitteeMembersUpdateView(UpdateView):
    model = CommitteeMembers
    # form_class = CommitteeMembersForm
    fields = ['member_name', 'position', 'description', 'image']
    template_name = 'committee_members/form.html'
    context_object_name = 'committee_member'
    success_url = reverse_lazy('accounts:committee-members-list')

class CommitteeMembersDeleteView(DeleteView):
    model = CommitteeMembers
    template_name = 'committee_members/delete.html'
    context_object_name = 'committee_member'
    success_url = reverse_lazy('committee-members-list')



from django.templatetags.static import static
def get_json_team(request):
    members = CommitteeMembers.objects.all()
    try:
        serialized_data = [
            {
                'Name':member.member_name,
                'Position': member.position,
                'Description': member.description,
                'Image': static(member.image.url) if member.image else ''
            }
        for member in members 
        ] 
        data = json.dumps(serialized_data)
        print(data)
        return JsonResponse({'data': data})
    except CommitteeMembers.DoesNotExist:
        return JsonResponse({'Error': 'No members'})
    












# class LoginView(View):
#     template_name = 'registration/login.html'
#     def post(self, request):
#         email    = form.cleaned["email"]
#         password = request.POST["password"]
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             redirect('home_page')
        
#         else:
#             messages.error(request, 'There was an error')
#         return render(request, self.template_name, {})
#     def get(self, request):
#         return render(request, self.template_name, {})
# # class LoginView(View):
# #     template_name = 'registration/login.html'
# #     form_class = CustomUserLoginForm
    
# #     def get(self, request):
# #         form = self.form_class()
# #         message = ''
# #         return render(request, self.template_name, context={'form': form, 'message': message})
        
# #     def post(self, request):
# #         form = self.form_class(request.POST)
# #         if form.is_valid():
# #             user = authenticate(
# #                 email=form.cleaned_data['email'],
# #                 password=form.cleaned_data['password'],
# #             )
# #             if user is not None:
# #                 login(request, user)
# #                 return redirect('home')
# #         message = 'Login failed!'
# #         return render(request, self.template_name, context={'form': form, 'message': message})

# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         success(request, "You have been logged out.")
#         return redirect('login')

# class CustomPasswordChangeView(PasswordChangeView):
#     template_name = 'registration/password_change_form.html'
#     success_url = reverse_lazy('membership:membership-list')

# class CustomPasswordResetView(PasswordResetView):
#     template_name           = 'registration/password_reset_form.html'
#     email_template_name     = 'registration/password_reset_email.html'
#     subject_template_name   = 'registration/password_reset_subject.txt'
#     success_url             = reverse_lazy('account:password_reset_done')

# class CustomPasswordResetConfirmView(PasswordResetConfirmView):
#     template_name = 'registration/password_reset_confirm.html'
#     success_url   = reverse_lazy('account:password_reset_complete')

# class CustomPasswordResetCompleteView(PasswordResetCompleteView):
#     template_name = 'registration/password_reset_complete.html'


# class CustomPasswordResetDoneView(PasswordResetDoneView):
#     template_name = 'registration/password_reset_done.html'  




# def login_view(request):
#     if request.method == "POST":
#         form = CustomUserLoginForm(request.POST)
#         if form.is_valid():
#             # username = form.cleaned_data['username']
#             email    = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f"Hi {user}")
#                 return redirect('membership:membership-list')
#             else:
#                 messages.error(request, f"There were errors in your the form")
#     else:
#         form = CustomUserLoginForm()       
#     return render(request, 'registration/login.html', {'form': form})


# def logout_view(request):
#     logout(request)
#     return redirect('home_page')

# @login_required
# def change_password(request):
#     form = PasswordChangeForm(request.user, request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             messages.success(request, 'Password Changed successfully')
#             return redirect('membership:membership-list')
#         else:
#             messages.error(request, 'Please correct the error')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'registration/password_change_form.html', {'form': form})

