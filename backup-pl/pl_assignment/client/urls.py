from django.conf.urls import url
from client.session_views import *
from client.views import *


def landing_redirector(request):
    """
    Redirect to home or login as required.
    """
    if request.user.is_anonymous:
        return redirect('/client/login')

    return redirect('/client/index')


app_name = 'services'
urlpatterns = [
    url(r'^$', landing_redirector),
    url(r'^login$', login_view),
    url(r'^index$', admin_home),
    url(r'^rack$', book_rack),
    url(r'^logout$', logout_view),
]
