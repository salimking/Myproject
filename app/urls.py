from django.shortcuts import render

# Create your views here.
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home' ),
    path('blog',views.blog,name='blog' ),
    path('contact',views.contact,name='contact' ),
    path('doctors',views.doctors,name='doctors' ),
    path('services',views.services,name='services' ),
    path('about',views.about,name='about' ),

    path('blog_single',views.blog_single,name='blog_single' ),
    path('appointment',views.Appointment,name='appointment'),

]
