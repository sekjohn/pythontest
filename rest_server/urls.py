from django.contrib import admin
from django.urls import path, include
from rest_framework import DefaultRouter
from teststart  import views


router = DefaultRouter()
router.register('post',views.PostViewSet)

urlpatterns = [
    path('',include(router.url)),
]