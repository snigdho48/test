from django.urls import path
from django.conf.urls import url
from .import views


urlpatterns = [

    url(r'^Signup/',views.Signup,name="Signup"),
    url(r'^Signin/',views.Signin,name="Signin"),
    url(r'^logout/',views.logout,name="logout"),

    ]
