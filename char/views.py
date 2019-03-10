from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from random import randint

from .models import Experience, Character, CharacterExperiences
from .forms import CharacterExperienceAddForm

@login_required
def home(request, notification=""):
    char = Character.objects.get(user=request.user)
    context = {
        'char': char,
    }
    if len(notification) > 0:
        context['notification'] = notification
    return render(request, 'char/home.html', context)

@login_required
def addExp(request):
    context = {}
    expAddForm = CharacterExperienceAddForm()
    context['expAddForm'] = expAddForm
    context['welcomeMessage'] = "Add an Experience"
    return render(request, 'char/add.html', context)

@csrf_exempt
def ajaxAdd(request):
    submission = request.POST.dict()
    toReturn = ''
    context = {}
    c = Character.objects.get(user=request.user)
    if timezone.now() >= c.lastTimeExperienced + timezone.timedelta(minutes=15):
        if submission['type'] == 'exp':
            e = Experience(description = submission['exp-description'], type = submission['stat'], experienceDate = timezone.now())
            e.save()
            ce = CharacterExperiences(character = request.user.character, experience = e)
            currentStat = getattr(request.user.character, submission['stat'])
            setattr(request.user.character, submission['stat'], currentStat+1)
            setattr(request.user.character, 'lastTimeExperienced', timezone.now())
            ce.save()
            toReturn = "Exp Added!"
        elif submission['type'] == 'work':
            currentStat = getattr(request.user.character, 'money')
            setattr(request.user.character, 'money', currentStat + randint(1, 9))
            setattr(request.user.character, 'lastTimeExperienced', timezone.now())
            toReturn = 'Worked!'
        elif submission['type'] == 'eat':
            currentHealth = getattr(request.user.character, 'health')
            if 'balanced-meal' in submission:
                setattr(request.user.character, 'health', currentHealth+1)
            else:
                setattr(request.user.character, 'health', currentHealth-1)
            if 'company' in submission:
                currentStat = getattr(request.user.character, 'SOC')
                setattr(request.user.character, 'SOC', currentStat+1)
            toReturn = 'Worked!'
        else:
            toReturn = 'nothing'

        if submission['weather'] != 'none':
            print(submission['weather'])
            currentStat = getattr(request.user.character, submission['weather'])
            setattr(request.user.character, submission['weather'], currentStat+1)
            
        request.user.character.save()
    else:
        toReturn = "15min"
    return HttpResponse(toReturn)
