from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        PhoneNumber = request.POST.get('PhoneNumber')
        WorkHours = request.POST.get('WorkHours')
        Gender = request.POST.get('Gender')
        Address = request.POST.get('Address')
        UserData = User(Name=Name, WorkHours=WorkHours, Address=Address, PhoneNumber=PhoneNumber, Gender=Gender)
        UserData.save()
        return HttpResponseRedirect('/')
    return render(request, 'register.html')