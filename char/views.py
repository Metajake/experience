from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Experience, Character
from .forms import ExperienceAddForm

@login_required
def home(request):
    char = Character.objects.get(user=request.user)
    exps = Experience.objects.filter(character=request.user.character)
    context = {
        'char': char,
        'exps': exps,
    }
    return render(request, 'char/home.html', context)

@login_required
def addExp(request):
    if request.method == "POST":
        expAddForm = ExperienceAddForm(request.POST)
        if expAddForm.is_valid():
            newExp = expAddForm.save(commit=False)
            newExp.experienceDate = timezone.now()
            newExp.character = request.user.character
            # print(request.user.character['STR'])
            print(type(request.POST.get('type')))
            # request.user.character[request.POST.get('type')] += 1
            currentStat = getattr(request.user.character, request.POST.get('type'))
            setattr(request.user.character, request.POST.get('type'), currentStat+1)
            request.user.character.save()
            newExp.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        expAddForm = ExperienceAddForm()
        context = {
            'expAddForm' : expAddForm,
        }
    context['welcomeMessage'] = "Add an Experience"
    return render(request, 'char/add.html', context)
