from django.shortcuts import render, redirect
from .forms import CreateUserForms, LoginForm

# Authentications forms import

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Import necessary functions, forms, and modules from Django


def homepage(request):

    return render(request, 'crm/index.html')
# Define a view function 'homepage' that renders the 'index.html' template


def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        # Create a login form instance and populate it with submitted data

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Extract username and password from the submitted form

            user = authenticate(request, username=username, password=password)
            # Authenticate user using provided username and password

            if user is not None:
                auth.login(request, user)
                # If the user is authenticated, log in the user
                return redirect("dashboard")
                # Redirect to the dashboard upon successful login
    context = {'loginform': form}
    # Prepare the form to be sent to the 'my-login.html' template
    return render(request, 'crm/my-login.html', context=context)
    # Render the 'my-login.html' template along with the context


def register(request):
    form = CreateUserForms()

    if request.method == "POST":
        form = CreateUserForms(request.POST)
        # Create a user registration form and populate it with submitted data

        if form.is_valid():
            form.save()
            # If the form data is valid, save the user registration details

            return redirect('my-login')
            # Redirect to the login page after successful registration

    content = {'registerform': form}
    # Prepare the form to be sent to the 'register.html' template
    return render(request, 'crm/register.html', context=content)
    # Render the 'register.html' template along with the context

def user_logout(request):
    auth.logout(request)
    # Logout the user

    return redirect("")
    # Redirect the user to the 'index' page after logging out
@login_required(login_url="my-login")
def dashboard(request):
    return render(request, 'crm/dashboard.html')
# Define a view function 'dashboard' that renders the 'dashboard.html' template



