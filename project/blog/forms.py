from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blog.models import UserProfileInfo
from django.db import models


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=True,max_length=100)
    birthday = forms.DateField(help_text='Format:YYYY-MM-DD')
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
    gender =forms.ChoiceField(choices=GENDER_CHOICES)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','birthday', )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.birthday = self.cleaned_data['birthday']
        user.gender = self.cleaned_data['gender']
        if commit:
            user.save()

        return user



# class RegistrationForm(forms.ModelForm):

#     class Meta:
#         model = UserProfileInfo
#         fields = ('firstname', 'lastname', 'email', 'password', 'birthday', 'gender',)

# def clean(self):
#         cleaned_data = super(ContactForm, self).clean()
#         name = cleaned_data.get('name')
#         email = cleaned_data.get('email')
#         message = cleaned_data.get('message')
#         if not name and not email and not message:
#             raise forms.ValidationError('You have to write something!')
