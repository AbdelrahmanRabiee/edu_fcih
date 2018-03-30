from django.db import models

# Create your models here.

type_choices = (('Academic', 'Academic'),
                ('Administrative', 'Administrative'),

                )

for_choices = (('All', 'All'),
                ('Students', 'Students'),
                ('Doctors', 'Doctors'),

                )

class Announcement(models.Model):
    an_type         = models.CharField(max_length=50, null=True, blank=True,choices=type_choices)
    an_for          = models.CharField(max_length=50, null=True, blank=True,choices=for_choices)
    an_subject      = models.CharField(max_length=150, null=True, blank=True)
    an_description  = models.TextField(max_length=1250, null=True, blank=True)
    created         = models.DateTimeField(null=True, auto_now_add=True)
    date            = models.DateField(null=True, auto_now_add=True)


    def __str__(self):
        return self.an_subject

    def __unicode__(self):
        return self.an_subject