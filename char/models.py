from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Character(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthDate = models.DateField(null=True, blank=True, auto_now=True)
    lastTimeExperienced = models.DateTimeField(blank=True)
    DKR = models.IntegerField(default=0)
    STR = models.IntegerField(default=0)
    DEX = models.IntegerField(default=0)
    VIT = models.IntegerField(default=0)
    END = models.IntegerField(default=0)
    INT = models.IntegerField(default=0)
    SOC = models.IntegerField(default=0)
    EMO = models.IntegerField(default=0)
    SPR = models.IntegerField(default=0)
    def __str__(self):
        return str(self.user)

class Experience(models.Model):
    experienceDate = models.DateTimeField("Date Experienced", auto_now=True)
    type = models.CharField(max_length=50)
    description = models.TextField()
    character = models.ForeignKey(Character, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.description

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Character.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.character.save()
