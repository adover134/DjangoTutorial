from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout


def main(request):
    print(request.user)
    return render(request, 'main.html')


def login(request):
    print(request.user)
    return render(request, 'main.html')


def logout(request):
    auth_logout(request)
    return redirect('/')


def test(request):
    return render(request, 'test.html')
