from django.contrib import admin

from .models import Membership, MembershipInterest

admin.site.register(MembershipInterest)
admin.site.register(Membership)
