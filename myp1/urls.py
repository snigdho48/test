"""myp1 URL Configuration

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
from django.conf.urls import url
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    url(r'^index/$',views.index,name="index"),
    url(r'^Blog/$',views.Blog,name="Blog"),
    url(r'^Help/$',views.Help,name="Help"),
    url(r'^Shop/$',views.Shop,name="Shop"),
    url(r'^Signin/$',views.Signin,name="Signin"),
    url(r'^Signup/$',views.Signup,name="Signup"),
    url(r'^Track/$',views.Track,name="Track"),
    url(r'^essential/$',views.essential,name="essential"),
    url(r'',views.cont1,name="cont1"),
    

]
