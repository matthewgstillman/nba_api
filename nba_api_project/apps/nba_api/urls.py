from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^players$', views.players),
    url(r'^stats$', views.stats),
    url(r'^games$', views.games),
]