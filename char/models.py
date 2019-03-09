from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Experience(models.Model):
    experienceDate = models.DateTimeField("Date Experienced", auto_now=True)
    type = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.description

class Character(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthDate = models.DateField(null=True, blank=True, auto_now=True)
    money = models.IntegerField(default = 0)
    lastTimeExperienced = models.DateTimeField(blank=True, default=timezone.now)
    experiences = models.ManyToManyField(
        Experience,
        through = 'CharacterExperiences',
        blank = True,
    )
    DRK = models.IntegerField(default=0)
    STR = models.IntegerField(default=0)
    DEX = models.IntegerField(default=0)
    VIT = models.IntegerField(default=0)
    END = models.IntegerField(default=0)
    INT = models.IntegerField(default=0)
    SOC = models.IntegerField(default=0)
    EMO = models.IntegerField(default=0)
    SPR = models.IntegerField(default=0)
    cold = models.IntegerField(default=0)
    hot = models.IntegerField(default=0)
    dry = models.IntegerField(default=0)
    wet = models.IntegerField(default=0)
    def __str__(self):
        return str(self.user)

class CharacterExperiences(models.Model):
    experience = models.ForeignKey(
        Experience,
        verbose_name="Experience",
        on_delete=models.PROTECT,
    )
    character = models.ForeignKey(
        Character,
        verbose_name="Character",
        on_delete=models.PROTECT
    )
    class Meta:
        verbose_name = "Character Experience"
        verbose_name_plural = "Character Experiences"
