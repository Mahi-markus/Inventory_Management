from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login
from django.contrib import messages


from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PropertyOwnerSignupForm

def property_owner_signup(request):
    if request.method == 'POST':
        form = PropertyOwnerSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sign-up request submitted successfully!")
            return redirect('property_owner_signup')  # Redirect to a confirmation page or refresh
    else:
        form = PropertyOwnerSignupForm()
    return render(request, 'property_owner_signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('user_dashboard')  # Redirect to the dashboard
        else:
            messages.error(request, "Invalid username or password!")
    return render(request, 'login.html')


@login_required
def user_dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})