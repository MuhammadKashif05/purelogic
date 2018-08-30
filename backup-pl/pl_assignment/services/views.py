from django.shortcuts import render, redirect
from django.contrib import messages as django_messages
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
        return redirect('/admin/login')
    if request.user.is_superuser:
        search_string = request.GET.get('search_string') if 'search_string' in request.GET else None
        if search_string is not None:
            return admin_render(request, 'index', {
                'books': RackBook.objects.filter(Q(book__title__icontains=search_string)|
                                             Q(book__author_name__icontains=search_string)|
                                             Q(book__publish_year=search_string)|
                                             Q(rack__name__icontains=search_string)).order_by('-id'),
                'type': 0,
            })

        return admin_render(request, 'index', {
            'books': Book.objects.all().order_by('-id'),
            'type': 1 ,
        })


def book_rack(request):
    if request.user.is_anonymous():
        return redirect('/admin/login')
    if request.user.is_superuser:
        return admin_render(request, 'rack', {
            'access': True,
            'racks': Rack.objects.all().order_by('-id'),
        })


def add_book(request):
    if request.user.is_anonymous():
        return redirect('/admin/login')
    if request.user.is_superuser:
        if request.method=='POST':
            title = request.POST['title']
            author = request.POST['author']
            year = request.POST['year']
            rack = request.POST['rack']

            book = Book.objects.create(
                title=title,
                author_name=author,
                publish_year=int(year)
            )
            rack = Rack.objects.get(id=rack)

            if RackBook.objects.filter(rack=rack).count() == 10:
                RackBook.objects.create(
                    book=book,
                    rack=rack,
                )
            else:
                return admin_render(request, 'add_book',{
                    'message': 'No more than 10 book in rack.',
                    'success':False
                })

        return admin_render(request, 'add_book', {
            'racks': Rack.objects.all().order_by('-id')
        })


def add_rack(request):
    if request.user.is_anonymous():
        return redirect('/admin/login')
    if request.user.is_superuser:
        if request.method=='POST':
            name = request.POST['name']
            print("request.POST['name']",request.POST['name'])
            Rack.objects.create(name=name)

        return admin_render(request, 'add_racks')
