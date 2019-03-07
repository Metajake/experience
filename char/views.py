from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Experience, Character
from .forms import ExperienceAddForm

@login_required
def home(request, notification=""):
    char = Character.objects.get(user=request.user)
    exps = Experience.objects.filter(character=request.user.character)
    context = {
        'char': char,
        'exps': exps,
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
            expAddForm = ExperienceAddForm(request.POST)
            if expAddForm.is_valid():
                newExp = expAddForm.save(commit=False)
                newExp.experienceDate = timezone.now()
                newExp.character = request.user.character
                currentStat = getattr(request.user.character, request.POST.get('type'))
                setattr(request.user.character, request.POST.get('type'), currentStat+1)
                setattr(request.user.character, 'lastTimeExperienced', timezone.now())
                request.user.character.save()
                newExp.save()
                return redirect('/')
            else:
                return redirect('/')
        else:
            context['notification'] = "Hasn't been 15 minutes."
            context['char'] = Character.objects.get(user=request.user)
            return redirect('Hasn\'t been 15 minutes.', context)
    else:
        expAddForm = ExperienceAddForm()
        context['expAddForm'] = expAddForm
    context['welcomeMessage'] = "Add an Experience"
    return render(request, 'char/add.html', context)
