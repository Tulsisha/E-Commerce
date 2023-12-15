"""demodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.Home),
    path('home',views.Home),
    path('about',views.about),
    path('services',views.services),
    path('contact',views.contact),
    path('register',views.register),
    path('contactform',views.contactform1),
    path('registeruser',views.registeruser),
    path('loginform',views.loginform),
    path('userhome',views.userhome),
    path('userlogout',views.userlogout),
    path('addrecord',views.addrecord),
    path('addcontact',views.addcontact),
    path('completerecord',views.completerecord),
    path('searchrecord',views.searchrecord),
    path('usersearchrecord',views.usersearchrecord),
    path('deleterecord',views.deleterecord),
    path('erase',views.erase),
    path('updaterecord',views.update),
    path('userupdate',views.userupdate),
    path('changepassword',views.changepassword),
    path('userchangepassword',views.userchangepassword),
    path('removed',views.removed),
    path('undorecord',views.undorecord),
    path('permanent',views.permanent),
    
]
