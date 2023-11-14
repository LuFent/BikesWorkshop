from django.shortcuts import render


def user_login_form(request):
    return render(request, "login.html")