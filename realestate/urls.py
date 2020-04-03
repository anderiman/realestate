"""realestate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from hamahang import views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('sale/',views.vw_sale,name='sale'),
    path('rents/',views.vw_rents,name='rents'),
    path('sale_apartement/',views.vw_apartement,name='sale_apartement'),
    path('sale_home/',views.vw_home,name='sale_home'),
    path('sale_land/',views.vw_land,name='sale_land'),
    path('participation/',views.vw_participation,name='participation'),
    path('Contact/',views.vw_Contact,name='Contact'),
    path('kish/',views.vw_kish,name='kish'),
    path('georgin/',views.vw_georgin,name='georgin'),
    path('mashhad/',views.vw_mashhad,name='mashhad'),
]
