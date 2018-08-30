from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


TEMPLATES = 'services/%s.html'


def admin_render(request, page, args = None, template = None):
    """
    Wrapper around render() which adds a page. If 'template' is None, the page
    name is used for the template.
    """
    if args == None:
        args = {}
    args['page'] = page
    if not template:
        template = page
    return render(request, TEMPLATES % template, args)


class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError('Your account is disabled')


def login_view(request):
    """
    This view allows a user to login.
    """
    if request.method == 'POST':

        print "request.POST",request.POST
        form = LoginForm(None, data=request.POST)
        if form.is_valid():
            user = form.get_user()

            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect('/client/index')
        else:
            return admin_render(request, 'customer_login', {
                'next': request.GET.get('next'),
                'form': form,
                'no_access': True,
            })

    else:
        form = LoginForm()
    return admin_render(request, 'customer_login', {
        'next': request.GET.get('next'),
        'form': form,
        'no_access': True,
    })


def logout_view(request):
    """
    Logout and redirect to login page.
    """
    logout(request)
    return redirect('/client/login')