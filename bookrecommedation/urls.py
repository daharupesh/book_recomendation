from django.contrib import admin
from django.urls import path , include
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('',include('authentication.urls')),
    path('',include('mainsystem.urls')),
  
]
