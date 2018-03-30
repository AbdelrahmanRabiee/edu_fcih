from django import forms


type_choices = (('Academic', 'Academic'),
                ('Administrative', 'Administrative'),

                )

for_choices = (('All', 'All'),
                ('Students', 'Students'),
                ('Doctors', 'Doctors'),

                )

class CreateAnnouncementForm(forms.Form):
    an_type     = forms.ChoiceField(required=True,choices=type_choices)
    an_for      = forms.ChoiceField(required=True,choices=for_choices)
    an_subject  = forms.CharField(required=True,widget=forms.TextInput(
        attrs={
            "placeholder": "subject ..."
        }
    ))
    an_description = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            "placeholder": "write your announcement here ..."
        }
    ))
