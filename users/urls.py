from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from django.urls import path

from users.views import UserListView, UserRegistrationView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', UserRegistrationView.as_view(), name='register'),
    path('list/', UserListView.as_view(), name='list'),
]

