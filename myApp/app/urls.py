from django.conf.urls import include, url
from app import views
urlpatterns = [
    url(r'^$', views.main,name='m'),
]