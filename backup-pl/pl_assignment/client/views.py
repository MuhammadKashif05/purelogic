from django.shortcuts import render, redirect
from client.models import *
from django.db.models import Q


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


def admin_home(request):
    if request.user.is_anonymous():
        return redirect('/client/login')

    search_string = request.GET.get('search_string') if 'search_string' in request.GET else None
    if search_string is not None:
        return admin_render(request, 'customer_index', {
            'books': RackBook.objects.filter(Q(book__title__icontains=search_string)|
                                         Q(book__author_name__icontains=search_string)|
                                         Q(book__publish_year=search_string)|
                                         Q(rack__name__icontains=search_string)).order_by('-id'),
            'type': 0,
        })

    return admin_render(request, 'customer_index', {
        'books': Book.objects.all().order_by('-id'),
        'type': 1 ,
    })


def book_rack(request):
    if request.user.is_anonymous():
        return redirect('/client/login')

    return admin_render(request, 'customer_rack', {
        'access': True,
        'racks': Rack.objects.all().order_by('-id'),
    })