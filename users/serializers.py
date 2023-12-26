from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """
       Serializer for the User model.
    """

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('email', 'password', 'is_active')
        read_only_fields = ('is_active', )
