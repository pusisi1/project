"""project URL Configuration

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
import project.views as views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',views.main),
    
    
    path('sub/',views.sub),
    path('text/',views.text),
    path('movie/',views.movie),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('korea/',views.korea),
    path('norway/',views.norway),
    path('bbc/',views.bbc),
    path('korea_data/',views.korea_test),
    path('norway_data/',views.norway_test),
    path('bbc_data/',views.bbc_data),
    
    
    #path('korea_data/', views.korea_data),
    #path('norway_data/', views.norway_data),
    #path('bbc_data/', views.bbc_data),
    
]
