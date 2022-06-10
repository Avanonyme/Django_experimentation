from django.contrib import admin
from django.urls import path, include
from help import views
urlpatterns=[
    path('',views.help)
]