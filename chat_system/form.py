from django import forms
from django.contrib.auth.models import Group,User

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