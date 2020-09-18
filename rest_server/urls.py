from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teststart  import views



urlpatterns = [
    path('post/', views.PostListAPIView.as_view()),
    path('post/<int:pk>', views.PostDetailAPIView.as_view())
    path('accounts/', include('accounts.urls')),
]