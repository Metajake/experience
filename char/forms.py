from django import forms

from .models import Experience

class ExperienceAddForm(forms.ModelForm):
    description = forms.CharField()
    type = forms.ChoiceField(choices = (
        ('STR','Strength'),
        ('INT','Intellect'),
        ('EMO', 'Emotion'),
        ('VIT', 'Vitality'),
        ('DEX', 'Dexterity'),
        ('SPR', 'Spirit'),
        ('SOC', 'Social'),
        ('END', 'Endurance'),
    ))
    class Meta:
        model = Experience
        fields = ('description','type',)
