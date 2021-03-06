from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=255)

    class Meta:
        model = Profile
        fields = ('public',)
