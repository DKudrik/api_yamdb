from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]