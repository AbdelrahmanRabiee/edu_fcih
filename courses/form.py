from django import forms
from .models import Course,Term
from .models import Term
def validate_active(value):
    if value:
        qs = Term.objects.filter(active=True)
        if qs.exists():
            raise forms.ValidationError('There is an active term! PLZZ uncheck active box :)')
    return value
def validate_courses(values):

    if len(values) > 6:
        raise forms.ValidationError('Sorry you cant register more than 6 course plz contact your academic supervisor!')

    return values
class AddCourseForm(forms.Form):
    hours_choices = (('2', '2'),
                     ('3', '3'),
                     )
    name     = forms.CharField(required=True,widget=forms.TextInput(
        attrs={
            "placeholder":"introduction to computer science"
        }
    ))

    code     = forms.CharField(required=True,widget=forms.TextInput(
        attrs={
            "placeholder":"CS101"
        }
    ))
    credit_hours = forms.ChoiceField(required=True, choices=hours_choices)

    description     = forms.CharField(required=True,widget=forms.Textarea(
        attrs={
            "placeholder":"write course description"
        }
    ))


class AddTermForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder": "spring 2017"
        }
    ))
    description = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            "placeholder": "write course description"
        }
    ))

    courses = forms.ModelMultipleChoiceField(required=True,
              queryset=Course.objects.all().order_by('-created') )

    active  = forms.BooleanField(required=False,widget=forms.CheckboxInput,validators=[validate_active])


class RegisterCourseForm(forms.Form):
    term = Term.objects.filter(active=True)
    if term.exists():
        opened_courses=Term.objects.get(active=True).courses.all()
        courses = forms.ModelMultipleChoiceField(label='',
                                                 widget=forms.CheckboxSelectMultiple,
                                                 queryset=opened_courses
                                                 ,validators=[validate_courses])


