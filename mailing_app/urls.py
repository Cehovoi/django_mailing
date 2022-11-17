from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'send/', views.send, name='send'),
    url(r'opened/(?P<letter_id>[0-9]+)/', views.opened, name='opened'),
]