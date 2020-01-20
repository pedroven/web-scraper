from django.urls import path

from . import views

app_name = 'scrap'
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search')
]