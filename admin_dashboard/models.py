from django.db import models
from django.contrib.auth.models import User
import random
import os
from django.db.models.signals import post_delete,pre_save,post_save
from django.dispatch import receiver

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_img(instance,filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,21452541)
    name,ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "students/{final_filename}".format(final_filename=final_filename)

def upload_img_doc(instance,filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,21452541)
    name,ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "doctors/{final_filename}".format(final_filename=final_filename)



class Student_profile(models.Model):
    gender_choices = (('male','male'), ('female','female'))
    religion_choices = (('muslim','muslim'), ('christian','christian'))

    level_choices = (('Level 1', 'Level 1'),
                     ('Level 1 continue', 'Level 1 continue'),
                     ('Level 2', 'Level 2'),
                     ('Level 2 continue', 'Level 2 continue'),
                     ('Level 3', 'Level 3'),
                     ('Level 3 continue', 'Level 3 continue'),
                     ('Level 4', 'Level 4'),
                     ('Level 4 continue', 'Level 4 continue')
                     )

    user        = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
    first_name  = models.CharField(max_length=50,null=True,blank=True)
    last_name   = models.CharField(max_length=50, null=True, blank=True)
    gender      = models.CharField(max_length=50, null=True, blank=True,choices=gender_choices)
    date_birth  = models.DateField(null=True, blank=True)
    phone       = models.CharField(max_length=50, null=True, blank=True)
    email       = models.EmailField(max_length=100, null=True, blank=True)
    religion    = models.CharField(max_length=50, null=True, blank=True,choices=religion_choices)
    level       = models.CharField(max_length=50, null=True, blank=True,choices=level_choices)
    img         = models.ImageField(upload_to=upload_img,null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Doctor_profile(models.Model):
    gender_choices = (('male','male'), ('female','female'))
    religion_choices = (('muslim','muslim'), ('christian','christian'))
    university_choices = (('Helwan', 'Helwan'),
                          ('Cairo', 'Cairo'),
                          ('Ain Shams', 'Ain Shams'),
                          ('Mansora', 'Mansora'),
                          ('Alex', 'Alex'),
                          ('AUC', 'AUC'),
                          )

    user                 = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
    first_name           = models.CharField(max_length=50,null=True,blank=True)
    last_name            = models.CharField(max_length=50, null=True, blank=True)
    gender               = models.CharField(max_length=50, null=True, blank=True,choices=gender_choices)
    date_birth           = models.DateField(null=True, blank=True)
    phone                = models.CharField(max_length=50, null=True, blank=True)
    email                = models.EmailField(max_length=100, null=True, blank=True)
    religion             = models.CharField(max_length=50, null=True, blank=True,choices=religion_choices)
    img                  = models.ImageField(upload_to=upload_img_doc,null=True, blank=True)

    highest_degree       = models.CharField(max_length=50,null=True,blank=True)
    university_high      = models.CharField(max_length=50,null=True,blank=True,choices=university_choices)
    year_passed_high     = models.DateField(null=True, blank=True)
    gpa_high             = models.DecimalField(max_digits=5,decimal_places=2,default=0.00,null=True,blank=True)
    other_degree         = models.CharField(max_length=50, null=True, blank=True)
    university_other     = models.CharField(max_length=50, null=True, blank=True, choices=university_choices)
    year_passed_other    = models.DateField(null=True, blank=True)
    gpa_other            = models.DecimalField(max_digits=5,decimal_places=2,default=0.00,null=True,blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


@receiver(post_delete,sender=Student_profile)
def delete_student(sender,instance,**kwargs):
        user = User.objects.get(username=instance.user)
        user.delete()

# @receiver(post_save,sender=Student_profile)
# def delete_user(sender,created,instance,**kwargs):
#     if created:
#         print('yes')
#         # user = User.objects.get(username=instance.user)
#         # user.delete()

@receiver(post_delete,sender=Doctor_profile)
def delete_user(sender,instance,**kwargs):
    user = User.objects.get(username=instance.user)
    user.delete()


















