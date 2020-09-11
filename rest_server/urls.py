from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from teststart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snippets/', views.Postlist.as_view()),
]