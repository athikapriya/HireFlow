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
        fields = [
            "username", "email", "designation", "profile_image",
            "phone", "location", "bio",
            "skills", "experience_years", "education",
            "github", "linkedin"
        ]

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
                "placeholder": "e.g. Software Engineer"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "11 digit phone number",
                "inputmode": "numeric",
                "pattern": "[0-9]{11}",
                "maxlength": "11"
            }),

            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter location"
            }),

            "bio": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Write something about you",
                "rows": 3
            }),

            "skills": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "e.g. Python, Django, React"
            }),

            "experience_years": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Years of experience"
            }),

            "education": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "e.g. BSc in CSE"
            }),

            "github": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "GitHub profile URL"
            }),

            "linkedin": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "LinkedIn profile URL"
            }),

            "profile_image": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "id": "id_profile_image"
            }),
        }

        def clean_phone(self):
            phone = self.cleaned_data.get("phone")

            if phone:
                if not phone.isdigit():
                    raise forms.ValidationError("Phone must contain only numbers.")
                if len(phone) != 11:
                    raise forms.ValidationError("Phone must be exactly 11 digits.")

            return phone


# =============== Employer Profile form =============== 
class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username", "email", "designation", "profile_image",
            "phone", "location", "bio",
            "company_name", "company_website", "industry"
        ]

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
                "placeholder": "e.g. HR Manager / Founder"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "11 digit phone number",
                "inputmode": "numeric",
                "pattern": "[0-9]{11}",
                "maxlength": "11"
            }),

            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter location"
            }),

            "bio": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Write something about you",
                "rows": 3
            }),

            "company_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company name"
            }),

            "company_website": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://company.com"
            }),

            "industry": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "e.g. IT, Software, Finance"
            }),

            "profile_image": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/*",
                "id": "id_profile_image"
            }),
        }

        def clean_phone(self):
            phone = self.cleaned_data.get("phone")

            if phone:
                if not phone.isdigit():
                    raise forms.ValidationError("Phone must contain only numbers.")
                if len(phone) != 11:
                    raise forms.ValidationError("Phone must be exactly 11 digits.")

            return phone