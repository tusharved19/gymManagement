"""gymManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from gym.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('', Index, name='Home'),
    path('admin_login', Login, name='login'),
    path('logout', logout_admin, name='logout'),

    path('add', Add, name='add'),
    path('view', View, name='view'),
    path('delete_enquiry(?p<int:pid>)', Delete_Enquiry, name='delete_enquiry'),

    path('aequip', Aequip, name='aequip'),
    path('vequip', Vequip, name='vequip'),
    path('deleteequipment(?p<int:pid>)', DeleteEquipment, name='deleteequipment'),

    path('aplan', Aplan, name='aplan'),
    path('vplan', Vplan, name='vplan'),
    path('deleteplan(?p<int:pid>)', Deleteplan, name='deleteplan'),

    path('amember', Amember, name='amember'),
    path('vmember', Vmember, name='vmember'),
    path('deletemember(?p<int:pid>)', Deletemember, name='deletemember'),
]


