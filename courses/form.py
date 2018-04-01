from django import forms
from .models import Course
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