from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Experience
from .forms import ExperienceAddForm

@login_required
def home(request):
    exps = Experience.objects.filter(user=request.user)
    context = {
        'welcomeMessage': "Welcome "+str(request.user)+"!",
        'exps': exps,
    }
    return render(request, 'char/home.html', context)

@login_required
def addExp(request):
    if request.method == "POST":
        print(request.POST)
        expAddForm = ExperienceAddForm(request.POST)
        if expAddForm.is_valid():
            newExp = expAddForm.save(commit=False)
            newExp.experienceDate = timezone.now()
            newExp.user = str(request.user)
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
