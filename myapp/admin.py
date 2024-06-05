from django.contrib import admin

from myapp.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'address','mobile_number','email')
