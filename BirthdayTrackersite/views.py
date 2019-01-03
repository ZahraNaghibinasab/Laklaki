from django.shortcuts import render
from .models import Whole
from .forms import UserForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db import connection

# Create your views here.

# def hospital(request):
#     drugs = DrugStore.objects.filter(expiredDate='1398')
#     return render(request, 'hospitalsite/signUp.html', {'drugs': drugs})



def birthday(request):
    return render(request,'BirthdayTrackersite/birthday.html')

def success(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            whole = Whole.objects.filter(day=form.cleaned_data['day'],month=form.cleaned_data['month'])
            print(whole.values('event'))
    return HttpResponse("Success!")

