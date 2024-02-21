from django.db import models
from django.forms import ValidationError
import re
from django.conf import settings

def validate_postcode(postcode):
    regex = r'^[A-Z]{1,2}[0-9][0-9A-Z]?\s?[0-9][A-Z]{2}$'
    if not re.match(regex, postcode):
        raise ValidationError('Invalid postcode format')
    
class Address(models.Model):
    address_line_1  = models.CharField(max_length=120, blank=True, null=True)
    address_line_2  = models.CharField(max_length=120, null=True, blank=True)
    city            = models.CharField(max_length=120, blank=True, null=True)
    county          = models.CharField(max_length=120, blank=True, null=True)
    post_code       = models.CharField(max_length=9, validators=[validate_postcode])

    def __str__(self):
        return f"{self.post_code}"
    
class MembershipInterest(models.Model):
    designation_options = [
        ("Mr", "Mr"),
        ("Mrs", "Mrs"),
        ("Miss", "Miss"),
        ("Ms", "Ms"),
        ("Mx", "Mx"),
        ("Dr", "Dr"),
        ("Prof", "Prof"),
    ]
    qual_status_options = [
        ("Student", "Student"),
        ("Qualified", "Qualified"),
    ]
    title                   = models.CharField(max_length=255, choices=designation_options)
    first_name              = models.CharField(max_length=255)
    last_name               = models.CharField(max_length=255)
    place_of_work_study     = models.CharField(max_length=255)
    job_title               = models.CharField(max_length=255, blank=True, null=True)
    work_address            = models.TextField(max_length=255, blank=True, null=True)
    email                   = models.EmailField()
    qualification_status    = models.CharField(max_length=255, choices=qual_status_options)
    qualification           = models.CharField(max_length=255, blank=True, null=True)
    qualification_location  = models.CharField(max_length=255)
    year_of_qualification   = models.DateField(blank=True, null=True)
    other_qualifications    = models.CharField(max_length=255, blank=True, null=True)
    data_use_permission     = models.BooleanField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Membership(models.Model):
    membership      = models.ForeignKey(MembershipInterest, on_delete=models.CASCADE)
    amount          = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date    = models.DateField(auto_now_add=True)
    status          = models.CharField(max_length=255, choices=[('Paid','Paid'), ('Expired','Expired'),('Canceled','Canceled')])
    paid            = models.BooleanField(default=False) # boolean for the webhook
    stripe_id       = models.CharField(max_length=255, blank=True)# session id from stripe
    subscription_id = models.CharField(max_length=255, blank=True, null=True) # sub id from stripe
    invoice_id      = models.URLField(max_length=255, blank=True, null=True) # invoice url from stripe
    customer_id     = models.CharField(max_length=255, blank=True, null=True) # customer id from stripe
    joined          = models.DateField(auto_now_add=True)
    updated         = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.membership}, {self.status}"

    
    def get_stripe_url(self):
            if not self.stripe_id:
                # no payment associated
                return ''
            if '_test_' in settings.STRIPE_SECRET_KEY:
                # Stripe path for test payments
                path = '/test/'
            else:
                # Stripe path for real payments
                path = '/'
            return f'https://dashboard.stripe.com{path}payments/{self.stripe_id}'


