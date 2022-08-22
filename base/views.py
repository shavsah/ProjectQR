import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from base.forms import PersonalDataForm
from qrcode import make
from base.models import PersonalData


def index(request):
    obj = PersonalData.objects.all()
    context = {'obj': obj}
    return render(request, 'base/home.html', context)


# Registering user into the website
def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user_data')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


# Form for user to enter some personal information after sign up
def user_data(request):
    form = PersonalDataForm()
    if request.method == 'POST':
        form = PersonalDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            try:
                path = settings.MEDIA_ROOT
                os.mkdir(path)
            except OSError:
                pass
            img = make(form.cleaned_data['email'])
            img_name = request.user.username + '.png'
            img.save(settings.MEDIA_ROOT + '/' + img_name)
        return render(request, 'base/save_path.html')
    context = {'form': form}
    return render(request, 'base/user_data.html', context)


# Saving QR code image in DB
def save_path(request):
    personal_data = PersonalData.objects.last()
    personal_data.qr_image = request.user.username + '.png'
    personal_data.save()
    return redirect('index')
