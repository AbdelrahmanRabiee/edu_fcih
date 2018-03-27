from django import forms
from .models import Student_profile
from django.contrib.auth.models import Group


def validate_user_name(value):

    qs = Student_profile.objects.filter(user__username=value)
    if qs.exists():
        raise forms.ValidationError("username already has a profile")
    return value

def validate_first_name(value):
    count = len(value)
    if count > 25:
        raise forms.ValidationError(('name must not be more than 5 chars, %(count)s chars is not acceptable !'), params={'count': count},)


class AddStudentForm(forms.Form):
    user_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder": "Student ID"
        }
    ))

    password = forms.CharField(required=True,widget=forms.PasswordInput(
        attrs={
            "placeholder":"Password"
        }
    ))


gender_choices = (('male', 'male'), ('female', 'female'))
religion_choices = (('muslim', 'muslim'), ('christian', 'christian'))

level_choices = (('Level 1', 'Level 1'),
                     ('Level 1 continue', 'Level 1 continue'),
                     ('Level 2', 'Level 2'),
                     ('Level 2 continue', 'Level 2 continue'),
                     ('Level 3', 'Level 3'),
                     ('Level 3 continue', 'Level 3 continue'),
                     ('Level 4', 'Level 4'),
                     ('Level 4 continue', 'Level 4 continue')
                     )


class AddStudentProfileForm(forms.Form):


    user_name = forms.ModelChoiceField(
        queryset=Group.objects.get(name="Students").user_set.all().order_by('-id')
        ,validators=[validate_user_name])

    first_name = forms.CharField(required=True,widget=forms.TextInput(
        attrs={
            "placeholder":"First_Name"
        }
    ),validators=[validate_first_name])
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder": "last_Name"
        }
    ))
    gender = forms.ChoiceField(choices=gender_choices)
    date_birth = forms.DateField(widget=forms.DateInput(
        attrs={
            "id":"studentDOB"
        }
    ))
    phone = forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            "placeholder": "0114-1802558"
        }
    ))
    email = forms.CharField(required=False,widget=forms.EmailInput(
        attrs={
            "placeholder": "example@example.com"
        }
    ))
    religion = forms.ChoiceField(choices=religion_choices)
    level = forms.ChoiceField(choices=level_choices)
    img = forms.ImageField(required=False,widget=forms.FileInput)


'''
/*******************************************************************************/
'''


class AddDoctorForm(forms.Form):
    user_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder": "Doctor ID"
        }
    ))

    password = forms.CharField(required=True,widget=forms.PasswordInput(
        attrs={
            "placeholder":"Password"
        }
    ))

class AddDoctorProfileForm(forms.Form):
    university_choices = (('Helwan', 'Helwan'),
                          ('Cairo', 'Cairo'),
                          ('Ain Shams', 'Ain Shams'),
                          ('Mansora', 'Mansora'),
                          ('Alex', 'Alex'),
                          ('AUC', 'AUC'),
                          )

    user_name = forms.ModelChoiceField(
        queryset=Group.objects.get(name="Doctors").user_set.all().order_by('-id')
        ,validators=[validate_user_name])

    first_name = forms.CharField(required=True,widget=forms.TextInput(
        attrs={
            "placeholder":"First_Name"
        }
    ),validators=[validate_first_name])
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder": "last_Name"
        }
    ))
    gender = forms.ChoiceField(choices=gender_choices)
    date_birth = forms.DateField(widget=forms.DateInput(
        attrs={
            "id":"studentDOB"
        }
    ))
    phone = forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            "placeholder": "0114-1802558"
        }
    ))
    email = forms.CharField(required=False,widget=forms.EmailInput(
        attrs={
            "placeholder": "example@example.com"
        }
    ))
    religion = forms.ChoiceField(choices=religion_choices)
    img = forms.ImageField(required=False,widget=forms.FileInput)

    highest_degree = forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            "placeholder": "PHD"
        }
    ))
    university_high = forms.ChoiceField(choices=university_choices)
    year_passed_high = forms.DateField(widget=forms.DateInput(
        attrs={
            "id":"doctorDOB"
        }
    ))
    gpa_high = forms.DecimalField(required=False,widget=forms.TextInput)

    other_degree = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "MSC"
        }
    ))
    university_other = forms.ChoiceField(choices=university_choices)
    year_passed_other = forms.DateField(widget=forms.DateInput(
        attrs={
            "id":"doctor2DOB"
        }
    ))
    gpa_other = forms.DecimalField(required=False, widget=forms.TextInput)






