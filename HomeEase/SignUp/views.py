from django.shortcuts import render, redirect
from .models import User
# Create your views here.

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        # Add any additional fields you want to capture during signup
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error_message': 'Username already exists.'})
        else:
            # Create a new user and save it to the database
            user = User(firstname=firstname, lastname=lastname, username=username, password=password)
            user.save()
            # Redirect to the index page after successful signup
            return redirect('success')  # 'index' is the name of the URL pattern for the index.html page
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.filter(username=username, password=password).first()
        if user is not None:
            # Redirect to the index page after successful login
            return redirect('success')  # 'index' is the name of the URL pattern for the index.html page
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials.'})
    else:
        return render(request, 'login.html')

def success(request):
    return render(request, 'success.html')
