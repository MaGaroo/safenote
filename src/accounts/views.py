from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def login_view(request):
    login_failed = False
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("notes")
        login_failed = True
    return render(request, "accounts/login.html", {
        "error": login_failed,
    })


def logout_view(request):
    logout(request)
    return redirect("login")
