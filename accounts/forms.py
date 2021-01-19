from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Account

class CustomAccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email']

class CustomAccountChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ['email']

class CustomUserCreationFprm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)