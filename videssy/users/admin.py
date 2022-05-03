"""Always create a custom user model every time you 
start a new project. This is a registry for the model to be visible
in the admin panel. If you wish to add more fields to the user model, you may
then add those here in the fieldset as well."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as OldUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(OldUserAdmin):
    list_display = ('username', 'email')
