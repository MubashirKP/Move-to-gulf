from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^post/$', views.postjob, name='postjob'),
     url(r'^listing/$',views.listing, name = "joblisting"),
     url(r'^search/$',views.search, name = "joblisting"),
     url(r'^aboutus/$',views.aboutus, name = "aboutus"),
     url(r'^contact/$',views.contact, name = "contact"),
     url(r'^jobdetail/(?P<jobid>[^\/|$]+)?\/?$',views.jobdetail)
]