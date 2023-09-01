from django.urls import path
from . import views
from .serializers import ImageSerializer,MyModelSerializer
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('api/users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/upload',views.ImageUpload.as_view(),name="home"),

]
