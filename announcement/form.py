from django import forms


type_choices = (('Academic', 'Academic'),
                ('Administrative', 'Administrative'),

                )

for_choices = (('All', 'All'),
                ('Students', 'Students'),
                ('Doctors', 'Doctors'),

                )
def validate_subject(value):
    count = len(value)
    if count >120:
        raise forms.ValidationError(('subject must not be more than 120 chars, %(count)s chars is not acceptable !'),
                                    params={'count': count}, )
    return value

def validate_description(value):
    count = len(value)
    if count > 1200:
        raise forms.ValidationError(('subject must not be more than 1200 chars, %(count)s chars is not acceptable !'),
                                    params={'count': count}, )
    return value
class CreateAnnouncementForm(forms.Form):
    an_type     = forms.ChoiceField(required=True,choices=type_choices)
    an_for      = forms.ChoiceField(required=True,choices=for_choices)
    an_subject  = forms.CharField(required=True,widget=forms.TextInput(
        attrs={
            "placeholder": "subject ..."
        }
    ),validators=[validate_subject])
    an_description = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            "placeholder": "write your announcement here ..."
        }
    ),validators=[validate_description])
