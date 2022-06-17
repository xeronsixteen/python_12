from django.contrib import admin
from django.urls import path

from webapp.views import math

urlpatterns = [
    path("", math),
]
