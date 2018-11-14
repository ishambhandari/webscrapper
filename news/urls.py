from django.conf.urls import url
from django.contrib import admin

from django.urls import path
from .views import scrape, news_list

urlpatterns = [
    path('scrape/', scrape, name ='scrape'),
    path('home/', news_list, name='news_list'),

]
