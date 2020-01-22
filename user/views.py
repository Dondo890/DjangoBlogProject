from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
#User service Controller

def RegisterUser(request):
    #Check if there is post request
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid:
            #Save form
            form.save()
            messages.success(request, "User successfully created.")
            return redirect('login-page')
        else:
            messages.error(request, "Error encountering registration. Please try again.")
            return redirect('login-page')
    else:
        form = UserRegisterForm()

    return render(request, 'html/registeruser.html', {'form': form})
