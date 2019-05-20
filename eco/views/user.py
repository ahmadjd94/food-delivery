from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.base import View

from ..forms import UserLoginForm

# todo: issue in login and signup of existing users
class UserSignUp(View):
    def post(self, request):
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'user/signup.html', {'form': form})


class UserSignIn(View):
    def post(self, request):
            form = UserLoginForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')

    def get(self, request):
        form = UserLoginForm()
        return render(request, 'user/signin.html', {'form': form})


class UserLogout(View):
    def post(self, request):
            logout(request)
            return redirect('home')
