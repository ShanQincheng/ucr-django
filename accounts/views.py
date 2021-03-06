from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm


@require_http_methods(["GET", "POST"])
def register(request: HttpRequest) -> HttpResponse:

    if request.method == "GET":
        return render(request, "accounts/register.html")

    if (form := UserRegistrationForm(request.POST)).is_valid():
        user = form.save()
        auth_login(request, user)

        return redirect(reverse('computers:home'))

    # an invalid registration form was posted to here
    return render(request, "accounts/register.html")


@require_http_methods(["GET", "POST"])
def login(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, 'accounts/login.html')

    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
        except KeyError:
            # Redisplay the computer homepage
            return render(request, 'computers/home.html', {
                'error_message': "Please fulfill the login form.",
            })
        else:
            # credentials error
            if user is None:
                # Redisplay the computer homepage
                return render(request, 'computers/home.html', {
                    'error_message': "Login failed",
                })

            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the back button.
            auth_login(request, user)
            return redirect(reverse('computers:home'))

    # Request method neither GET nor POST, return to homepage
    return render(request, 'computers/home.html', {'error_message': "Wrong request method"})