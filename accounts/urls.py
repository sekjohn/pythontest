from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.contrib.auth.views import LoginView
from accounts import form

urlpatterns = [
    #path('api-token-auth/', obtain_auth_token),
    path('login/', LoginView.as_view(template_name='login_form.html'), name='login'),
    #path('api-jwt-auth/', obtain_jwt_token),
	#path('api-jwt-auth/refresh/', refresh_jwt_token),
	#path('api-jwt-auth/verify/', verify_jwt_token),
]
