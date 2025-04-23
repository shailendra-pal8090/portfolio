# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('contact/', contact_view, name='contact'),
]
