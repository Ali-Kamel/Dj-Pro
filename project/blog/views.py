from django.shortcuts import render, redirect
from django.contrib.auth import logout
from blog.forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm


def landing(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/admin/')
    else:
        form = RegistrationForm()
    context = {'form' : form}
    return render(request, "registration/01-landingPage.html",context)




def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/admin/')
    else:
        form = RegistrationForm()
    context = {'form' : form}
    return render(request,'registration/test_the_register.html',context )




def login(request):
    return render(request, "registration/01-landingPage.html")




def logout_view(request):
  logout(request)
  return render(request, 'registration/test_the_logout.html')