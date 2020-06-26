from django.contrib import admin
from django.urls import path,include
from tubeloader import views

app_name = 'tubeloader'

urlpatterns = [
    path('instavid/', views.insta,name='instavid'),
    path('get_link/',views.get_link,name='get_link'),
    path('get_insta/',views.get_insta,name='get_insta'),
    path('',views.redir,name='redir')
]