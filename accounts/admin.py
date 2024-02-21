from django.contrib import admin

from .models import CustomUser, CommitteeMembers

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_approved', 'last_login']
    list_filter = ['is_approved']
    actions = ['approve_users']

    def approve_users(self, request, queryset):
        queryset.update(is_approved=True)

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(CommitteeMembers)
