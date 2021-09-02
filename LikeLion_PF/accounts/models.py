from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib import auth

class Profile (models.Model) :
    user = models.OneToOneField(auth.models.User,on_delete=models.CASCADE,null=True)
   # username=models.CharField(max_length=10)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    image = models.ImageField(blank=True)

@receiver(post_save, sender=auth.models.User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=auth.models.User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
