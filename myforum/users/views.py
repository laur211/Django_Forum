from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import logout
# Create your views here.


def register(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('forum')

    else:
        userform = UserForm()
    return render (request, "users/users.html", {"userform":userform})


def logout_view(request):
    logout(request)
    return redirect ("login")
