from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django import forms


from .models import User


# =============== candidate register form =============== 
class CandidateRegisterForm(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control custom-input",
            "placeholder": "Enter Password"
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control custom-input",
            "placeholder": "Confirm Password"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control custom-input",
                "placeholder": "Username"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control custom-input",
                "placeholder": "Email"
            }),
        }




# =============== employer register form =============== 
class EmployerRegisterForm(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control custom-input",
            "placeholder": "Enter Password"
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control custom-input",
            "placeholder": "Confirm Password"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control custom-input",
                "placeholder": "Username"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control custom-input",
                "placeholder": "Email"
            }),
        }




# =============== custom password set form =============== 
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control custom-input",
            "placeholder": "Enter new password"
        })
    )

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control custom-input",
            "placeholder": "Confirm new password"
        })
    )


# =============== Candidate Profile form =============== 
class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "designation", "profile_image"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter username"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email"
            }),
            "designation": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your designation / title"
            }),
            "profile_image": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/*"
            }),
        }


# =============== Employer Profile Form ===============
class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "designation", "profile_image"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter username"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email"
            }),
            "designation": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter company / designation"
            }),
            "profile_image": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/*"
            }),
        }