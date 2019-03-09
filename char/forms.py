from django import forms

from .models import CharacterExperiences

class CharacterExperienceAddForm(forms.ModelForm):
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
        model = CharacterExperiences
        fields = ('description','type',)
