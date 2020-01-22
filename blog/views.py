from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here - Controller in Java.

#Controller for homepage
#Inject login required in page
@login_required
def HomePage(request):
    return render(request, 'html/home.html')

@login_required
def ProfilePage(request):
    return render(request, 'html/profile.html')
