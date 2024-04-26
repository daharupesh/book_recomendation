from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Sign in view
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, username+" Logged in successfully!")
            return redirect('signin')
        else:
            messages.error(request, "Invalid credentials!")
            
    return render(request, "login.html", {})

# Sign up view
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('signup')

        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.save()
        
        messages.success(request, username+ " account has been successfully created.")
        return redirect('signin')  # Redirect to the login page after successful registration

    return render(request, "register.html", {})


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('/')
