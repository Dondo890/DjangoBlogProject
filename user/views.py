from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
#User service Controller

def RegisterUser(request):
    #Check if there is post request
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            #Save form
            form.save()
            messages.success(request, "User successfully created.")
            return redirect('index')
        else:
            messages.error(request, "Error encountering registration. Please try again.")
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'html/registeruser.html', {'form': form})
