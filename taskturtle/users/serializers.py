from rest_framework import serializers
from users.models import User
from rest_auth.registration.serializers import RegisterSerializer


class CustomRegistrationSerialzier(RegisterSerializer):
    username = serializers.CharField(required=False)


class UserSerialzier(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'id', 'first_name', 'last_name']

