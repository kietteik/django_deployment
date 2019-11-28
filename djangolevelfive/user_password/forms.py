from django import forms
from django.contrib.auth.forms import User
from user_password.models import UserProfileInfo


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'username'})
        self.fields['email'].widget.attrs.update({'class': 'username'})

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileInfoForm, self).__init__(*args, **kwargs)
        self.fields['website'].label_classes = ('username')
        # self.fields['profile_pic'].widget.attrs.update(
        #     {'class': 'login-button'})
        self.fields['website'].widget.attrs.update({'class': 'username'})

    class Meta:
        model = UserProfileInfo
        fields = ('website', 'profile_pic')
