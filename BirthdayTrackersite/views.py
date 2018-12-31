from django.shortcuts import render



def birthday(request):
    return render(request,'BirthdayTrackersite/birthday.html')