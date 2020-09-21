from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teststart  import views
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('login/', LoginView.as_view(template_name='login_form.html'), name='login'),
    path('admin/', admin.site.urls),
    path('post/', views.PostListAPIView.as_view()),
    path('post/<int:pk>', views.PostDetailAPIView.as_view()),
    path('accounts/', include('accounts.urls')),
]