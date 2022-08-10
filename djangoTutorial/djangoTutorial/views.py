from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from customForms.customForm import TestForm


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
    return render(request, 'test.html', {'testForm': TestForm})


def upload_test(request):
    images = request.FILES.getlist('test4')
    for image in images:
        handle_uploaded_file(image, str(image))
    return redirect('test')


def handle_uploaded_file(f, name):
    with open('static/images/'+name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
