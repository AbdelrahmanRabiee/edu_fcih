from django import forms
from .models import Student_profile
from django.contrib.auth.models import Group,User

def validate_username(value):
    qs = User.objects.filter(username=value)
    count = len(value)
    if qs.exists():
        raise forms.ValidationError("username already exist")
    if count > 50:
        raise forms.ValidationError(('USER ID must not be more than 50 chars, %(count)s chars is not acceptable !'), params={'count': count},)
    return value


def validate_user_name(value):

    qs = Student_profile.objects.filter(user__username=value)
    if qs.exists():
        raise forms.ValidationError("username already has a profile")
    return value

def validate_first_name(value):
    count = len(value)
    if count > 25:
        raise forms.ValidationError(('name must not be more than 25 chars, %(count)s chars is not acceptable !'), params={'count': count},)
    return value
def validate_mail(value):
    if len(value)>100:
        raise forms.ValidationError('PLZ add valid email address')
    return value

def validate_user_password(value):
    count = len(value)
    if count>100:
        raise forms.ValidationError(('password must not be more than 100 chars, %(count)s chars is not acceptable !'), params={'count': count},)
    if sum(c.isdigit() for c in value) < 2:
        raise forms.ValidationError('Password must container at least 2 digits.')
    if not any(c.isupper() for c in value):
        raise forms.ValidationError('Password must container at least 1 uppercas')

    return value
def validate_phone(value):
    if sum(c.isdigit() for c in value) < 11:
        raise forms.ValidationError('Phone number must containe at least 11 digits.')
    if len(value)>20:
        raise forms.ValidationError('Enter a valid phone number')


class AddAdminForm(forms.Form):
    user_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder": "Admin ID"
        }
    ),validators=[validate_username])
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder": "First Name"
        }
    ),validators=[validate_first_name])
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder": "Last Name"
        }
    ),validators=[validate_first_name])
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            "placeholder": "example@example.com"
        }
    ),validators=[validate_mail])

    password = forms.CharField(required=True,widget=forms.PasswordInput(
        attrs={
            "placeholder":"Password"
        }
    ),validators=[validate_user_password])

class AddStudentForm(forms.Form):
    user_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder": "Student ID"
        }
    ),validators=[validate_username])

    password = forms.CharField(required=True,widget=forms.PasswordInput(
        attrs={
            "placeholder":"Password"
        }
    ),validators=[validate_user_password])


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

    first_name = forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            "placeholder":"First_Name"
        }
    ),validators=[validate_first_name])
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "last_Name"
        }
    ),validators=[validate_first_name])
    gender = forms.ChoiceField(choices=gender_choices)
    date_birth = forms.DateField(widget=forms.DateInput(
        attrs={
            "id":"studentDOB"
        }
    ))
    phone = forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            "placeholder": "01141802558"
        }
    ),validators=[validate_phone])
    email = forms.CharField(required=False,widget=forms.EmailInput(
        attrs={
            "placeholder": "example@example.com"
        }
    ),validators=[validate_mail])
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
    ),validators=[validate_username])

    password = forms.CharField(required=True,widget=forms.PasswordInput(
        attrs={
            "placeholder":"Password"
        }
    ),validators=[validate_user_password])

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

    first_name = forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            "placeholder":"First_Name"
        }
    ),validators=[validate_first_name])
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "last_Name"
        }
    ),validators=[validate_first_name])
    gender = forms.ChoiceField(choices=gender_choices)
    date_birth = forms.DateField(widget=forms.DateInput(
        attrs={
            "id":"studentDOB"
        }
    ))
    phone = forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            "placeholder": "01141802558"
        }
    ),validators=[validate_phone])
    email = forms.CharField(required=False,widget=forms.EmailInput(
        attrs={
            "placeholder": "example@example.com"
        }
    ),validators=[validate_mail])
    religion = forms.ChoiceField(choices=religion_choices)
    img = forms.ImageField(required=False,widget=forms.FileInput)

    highest_degree = forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            "placeholder": "PHD"
        }
    ),validators=[validate_first_name])
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
    ),validators=[validate_first_name])
    university_other = forms.ChoiceField(choices=university_choices)
    year_passed_other = forms.DateField(widget=forms.DateInput(
        attrs={
            "id":"doctor2DOB"
        }
    ))
    gpa_other = forms.DecimalField(required=False, widget=forms.TextInput)






