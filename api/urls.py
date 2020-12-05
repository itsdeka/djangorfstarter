from django.urls import include, path

from rest_framework_simplejwt import views as jwt

from api import views, serializers

urlpatterns = [
    path('users', views.Users.as_view()), path('users/<int:user>', views.user),

    path('token', jwt.TokenObtainPairView.as_view(serializer_class=serializers.JWTSerializer)),
    
    path('token/refresh', jwt.TokenRefreshView.as_view()), path('token/verify', jwt.TokenVerifyView.as_view()),
]