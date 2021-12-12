from django.contrib import admin

from . import models
from . import forms


@admin.register(models.SocialNetworkUser)
class SocialNetworkUserAdmin(admin.ModelAdmin):
    add_form = forms.SocialNetworkUserCreationForm
    form = forms.SocialNetworkUserChangeForm

    list_display = ["email", "username", "last_seen", "last_login"]
