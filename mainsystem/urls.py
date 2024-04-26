from django.contrib import admin
from django.urls import path , include
from .import views
urlpatterns = [
    # path('mainpage/', views.mainPage , name = "mainPage"),
    # path('signout/', views.signout , name = "signout"),
    path('mainpage/', views.index ,name= "index" ),

    
]
