from django import forms
from user.models import User


class AdduserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]