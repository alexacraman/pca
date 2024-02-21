from django import forms
from .models import MembershipInterest, Address, Membership



class InterestForm(forms.ModelForm):
    class Meta:
        model = MembershipInterest
        fields = ['title', 'first_name', 'last_name', 'place_of_work_study', 'job_title', 'work_address', 'email', 'qualification_status', 'qualification', 'qualification_location', 'year_of_qualification', 'other_qualifications', 'data_use_permission']
        widgets = {
            'title':forms.Select(
                attrs={'class':'p-2 rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue'}
            ),
            'first_name':forms.TextInput(
                attrs={'class':'p-2 rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue' }
            ),
            'last_name':forms.TextInput(
                attrs={'class':'p-2 rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue' }
            ),
            'place_of_work_study':forms.TextInput(
                attrs={'class':'p-2 rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue' }
            ),
            'job_title':forms.TextInput(
                attrs={'class':'p-2 rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue' }
            ),
            'work_address':forms.Textarea(
                attrs={'rows':2, 'cols':2, 'class':'p-2 rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue' }
            ),
            'email':forms.EmailInput(
                attrs={'class':'p-2 rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue' }
            ),
             'qualification_status':forms.Select(
                attrs={'class':'p-2 rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue'}
            ),
             'qualification':forms.TextInput(
                attrs={'class':'p-2 rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue' }
            ),
             'qualification_location':forms.TextInput(
                attrs={'class':'p-2 rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue' }
            ),
             'year_of_qualification':forms.DateInput(
                attrs={'type':'date', 'class':'p-2 rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue' }
            ),
             'other_qualifications':forms.TextInput(
                attrs={'class':'p-2 rounded-lg w-full my-4 shadow-sm shadow-white outline outline-2 outline-blue' }
            ),
            
        }

class Addressform(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_line_1', 'address_line_2', 'city', 'county', 'post_code']