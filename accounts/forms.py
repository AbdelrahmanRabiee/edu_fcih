from django import forms
from admin_dashboard.models import Student_profile,Doctor_profile
def validate_user_name(value):
    qs1 = Student_profile.objects.filter(user__username=value)
    qs2 = Doctor_profile.objects.filter(user__username=value)
    if not qs1.exists() and not qs2.exists():
        raise forms.ValidationError("USERNAME NOT FOUND 404")
    return value


class LoginForm(forms.Form):
    user_name = forms.CharField(required=True,widget=forms.TextInput(
        attrs={
                "class" :"form-control",
                "placeholder" :"Username/Email"

        }
    ),validators=[validate_user_name])
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Password"

        }
    ))