from rest_framework import generics
from users.permissions import IsSuperUser
from users.models import User

from users.serializers import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    """
    View to handle user registration.
    """

    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()


class UserListView(generics.ListAPIView):
    """
       View to list users (accessible only by superuser).
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser]



