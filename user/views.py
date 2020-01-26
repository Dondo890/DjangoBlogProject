from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
#User service Controller

def RegisterUser(request):
    #Check if there is post request
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
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

@login_required
def ProfilePage(request):

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile successfully updated.")
            return redirect('profile-page')
        else:
            message.error(request, "Error updating profile!")
            return redirect('profile-page')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'html/profile.html', context)
