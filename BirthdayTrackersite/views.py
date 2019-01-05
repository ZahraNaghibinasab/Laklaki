from django.shortcuts import render
from .models import Whole
from .models import Months
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
            month = Months.objects.filter(id=form.cleaned_data['month'])
            print(whole)
            print(month[0].symbol)
    return render(request, 'BirthdayTrackersite/event.html', {'whole': whole , 'monthsymbol': month[0].symbol , 'monthplanet': month[0].planet , 'monthcolor': month[0].color , 'monthrock': month[0].rock , 'monthchance':month[0].chanceDay})

