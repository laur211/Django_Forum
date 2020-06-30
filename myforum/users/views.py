from django.shortcuts import render, redirect
from .forms import UserForm
# Create your views here.

def register(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect ("forum")

    else:
        userform = UserForm()
    return render (request, "users/users.html", {"userform":userform})