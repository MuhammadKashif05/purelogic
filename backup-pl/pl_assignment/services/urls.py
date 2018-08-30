from django.conf.urls import url
from services.session_views import *
from services.views import *


def landing_redirector(request):
    """
    Redirect to home or login as required.
    """
    if request.user.is_anonymous:
        return redirect('/admin/login')

    return redirect('/admin/index')


app_name = 'services'
urlpatterns = [
    url(r'^$', landing_redirector),
    url(r'^login$', login_view),
    url(r'^index$', admin_home),
    url(r'^rack$', book_rack),
    url(r'^logout$', logout_view),
    url(r'^add_book', add_book),
    url(r'^add_rack', add_rack),
]
