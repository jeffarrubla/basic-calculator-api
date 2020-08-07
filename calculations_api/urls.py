"""calculations_api URL Configuration

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
from django.urls import path, include
from myapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('myapi.urls')),
    path('',views.index),
    path('api/',views.index),
    path('api/sum/<str:a>/<str:b>/',views.sum, name="sum"),
    path('api/subt/<str:a>/<str:b>/',views.subt, name="subtraction"),
    path('api/mul/<str:a>/<str:b>/',views.mul, name="multiplication"),
    path('api/div/<str:a>/<str:b>/',views.div, name="division"),
]
