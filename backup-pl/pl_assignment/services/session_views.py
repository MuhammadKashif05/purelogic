from .views import admin_render
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

TEMPLATES = '/services/%s.html'

class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError('Your account is disabled')


def login_view(request):
    """
    This view allows a user to login.
    """
    if request.method == 'POST':
        form = LoginForm(None, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST['next'])
                else:
                    return redirect('/admin/index')
        else:
            return admin_render(request, 'login', {
                'next': request.GET.get('next'),
                'form': form,
                'no_access': True,
            })

    else:
        form = LoginForm()

    return admin_render(request, 'login', {
        'next': request.GET.get('next'),
        'form': form,
        'no_access': True,
    })


def logout_view(request):
    """
    Logout and redirect to login page.
    """
    logout(request)
    return redirect('/admin/login')