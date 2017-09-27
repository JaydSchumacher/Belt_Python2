from django.conf.urls import url
from . import views

def test(request):
    print 710

urlpatterns = [
    url(r'^dashboard', views.dashboard),
    url(r'^add/(?P<id>\d+)$', views.add),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^show/(?P<id>\d+)$', views.show),
]