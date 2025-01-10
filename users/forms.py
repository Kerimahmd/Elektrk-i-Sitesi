from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model=User
        fields = ['username','password']
        
    username = forms.CharField()
    password = forms.CharField()


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields = ("first_name",
                  "last_name",
                  "email",
                  "username",
                  "password1",
                  "password2"
                )
        
    first_name = forms.CharField()
    last_name = forms.CharField()
    email= forms.CharField()
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()



class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("first_name",
                "last_name", 
                "username",
                "email",
                )
        
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()





    #username = forms.CharField(
    #    widget=forms.TextInput(attrs={"autofocus": True,
    #                                  'class': 'form-control',
    #                                  'placeholder': 'Kullanıcı Adınızı Girin'})
    #)
    #password = forms.CharField(
    #    widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                     'class': 'form-control',
    #                                      'placeholder': 'Şifrenizi Girin'})
    # )
