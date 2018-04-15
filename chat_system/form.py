from django import forms
from django.contrib.auth.models import Group,User

def validate_subject(value):
    count = len(value)
    if count >120:
        raise forms.ValidationError(('subject must not be more than 120 chars, %(count)s chars is not acceptable !'),
                                    params={'count': count}, )
    return value

def validate_content(value):
    count = len(value)
    if count > 1200:
        raise forms.ValidationError(('subject must not be more than 1200 chars, %(count)s chars is not acceptable !'),
                                    params={'count': count}, )
    return value

class SendMessageForm(forms.Form):
    reciever_student = forms.ModelChoiceField(required=False,
        queryset=Group.objects.get(name="Students").user_set.all().order_by('-id')
        )
    reciever_doctor = forms.ModelChoiceField(required=False,
        queryset=Group.objects.get(name="Doctors").user_set.all().order_by('-id')
    )
    message_subject = forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            "placeholder":"SUBJECT"
        }
    ))
    message_content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            "placeholder": "Feel free to write your MESSAGE ......."
        }
    ))


class StudentSendMessageForm(forms.Form):
    reciever_doctor = forms.ModelChoiceField(required=False,
        queryset=Group.objects.get(name="Doctors").user_set.all().order_by('-id')
    )

    message_subject = forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            "placeholder":"SUBJECT"
        }
    ),validators=[validate_subject])
    message_content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            "placeholder": "Feel free to write your MESSAGE ......."
        }
    ),validators=[validate_content])



class DoctorSendMessageForm(forms.Form):
    reciever_student = forms.ModelChoiceField(required=False,
        queryset=Group.objects.get(name="Students").user_set.all().order_by('-id')
        )
    reciever_admin = forms.ModelChoiceField(required=False,
        queryset=Group.objects.get(name="Admins").user_set.all().order_by('-id')
    )
    message_subject = forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            "placeholder":"SUBJECT"
        }
    ))
    message_content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            "placeholder": "Feel free to write your MESSAGE ......."
        }
    ))