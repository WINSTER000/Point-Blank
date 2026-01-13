from django.urls import path
from django.contrib import admin
from .views import Firearm

firearms = Firearm()

urlpatterns = [
    path('',firearms.home),
    path('about',firearms.about),
    path('arsenal',firearms.fetch_all_firearms),
    path('firearm_details',firearms.firearm_details),
]