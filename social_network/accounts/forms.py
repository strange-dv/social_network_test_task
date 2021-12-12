from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SocialNetworkUser


class SocialNetworkUserCreationForm(UserCreationForm):

    class Meta:
        model = SocialNetworkUser
        fields = ('username', 'email')


class SocialNetworkUserChangeForm(UserChangeForm):

    class Meta:
        model = SocialNetworkUser
        fields = ('username', 'email')
