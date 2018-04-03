from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#
# class TermQuerySet(models.QuerySet):
#
#     def active(self):
#         return self.filter(active=True)
#
# class TermManager(models.Manager):
#     def get_queryset(self):
#         return TermQuerySet(self.model,using=self._db)
#     def active(self):
#         return self.get_queryset().active()


hours_choices = (('2', '2'),
                ('3', '3'),

                )
class Course(models.Model):
    student         = models.ManyToManyField(User,
                                         blank=True,
                                         related_name="student")
    doctor          = models.ManyToManyField(User,
                                          blank=True,
                                         related_name="doctor")
    name            = models.CharField(max_length=120,null=True,blank=True)
    code            = models.CharField(max_length=120,null=True,blank=True)
    credit_hours    = models.CharField(max_length=12,null=True,blank=True,choices=hours_choices)
    description     = models.TextField(max_length=1200,null=True,blank=True)
    created         = models.DateTimeField(null=True, auto_now_add=True)
    passed          = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Term(models.Model):
    courses      = models.ManyToManyField(Course,blank=True)
    name        = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(max_length=1200, null=True, blank=True)
    created     = models.DateTimeField(null=True, auto_now_add=True)
    active      = models.BooleanField(default=False)

    # objects = TermManager()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
