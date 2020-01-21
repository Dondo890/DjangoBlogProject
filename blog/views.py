from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here - Controller in Java.

#Controller for homepage
def HomePage(request):
    return render(request, 'html/home.html')
