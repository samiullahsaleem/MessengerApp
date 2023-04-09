from django.shortcuts import render, redirect
from .forms import signupform
from django.contrib.auth import login, authenticate

# Create your views here.

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            return redirect('frontpage')
    else:
        form = signupform()
    return render(request, 'core/signup.html', {'form': form})