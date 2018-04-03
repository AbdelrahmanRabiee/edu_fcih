from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Message(models.Model):
    sender          = models.ForeignKey(User, related_name="sender", null=True,on_delete=models.CASCADE)
    reciever        = models.ForeignKey(User, related_name="receiver", null=True,on_delete=models.CASCADE)
    message_subject = models.CharField(max_length=250, null=True, blank=True)
    message_content = models.TextField(max_length=1250, null=True, blank=True)
    created         = models.DateTimeField(null=True, auto_now_add=True)
    date            = models.DateField(null=True, auto_now_add=True)

    def __str__(self):
        return self.message_content

    def __unicode__(self):
        return self.message_content

class MessageNotification(models.Model):
    notify_message = models.TextField(max_length=250, null=True, blank=True)
    created        = models.DateTimeField(null=True, auto_now_add=True)
    date           = models.DateField(null=True, auto_now_add=True)

    def __str__(self):
        return self.notify_message

    def __unicode__(self):
        return self.notify_message

@receiver(post_save,sender=Message)
def notify_sending_message(sender,created,instance,**kwargs):
    if created:
        sender = User.objects.get(username=instance.sender)
        reciever = User.objects.get(username=instance.reciever)
        message = str(sender) + ": has sent a message to: " + str(reciever)
        MessageNotification.objects.create(
            notify_message= message
        )
