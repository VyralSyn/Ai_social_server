from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('users/', include('users.urls')),  # User authentication endpoints
    path('posts/', include('posts.urls')),  # Blog posts or content API
    path('token/', obtain_auth_token, name='api_token_auth'), 
]
