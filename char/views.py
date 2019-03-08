from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Experience, Character, CharacterExperiences
from .forms import ExperienceAddForm, CharacterExperienceAddForm

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
    if request.method == "POST":
        c = Character.objects.get(user=request.user)
        if timezone.now() >= c.lastTimeExperienced + timezone.timedelta(minutes=15):
            expAddForm = CharacterExperienceAddForm(request.POST)
            if expAddForm.is_valid():
                newExp = expAddForm.save(commit=False)
                e = Experience(description = request.POST.get('description'), type=request.POST.get('type'), experienceDate = timezone.now())
                e.save()
                ce = CharacterExperiences(character=request.user.character,experience = e)
                currentStat = getattr(request.user.character, request.POST.get('type'))
                setattr(request.user.character, request.POST.get('type'), currentStat+1)
                setattr(request.user.character, 'lastTimeExperienced', timezone.now())
                request.user.character.save()
                print(ce)
                ce.save()
                return redirect('/')
            else:
                return redirect('/')
        else:
            context['notification'] = "Hasn't been 15 minutes."
            context['char'] = Character.objects.get(user=request.user)
            return redirect('note/Hasn\'t been 15 minutes.', context)
    else:
        expAddForm = CharacterExperienceAddForm()
        context['expAddForm'] = expAddForm
    context['welcomeMessage'] = "Add an Experience"
    return render(request, 'char/add.html', context)
