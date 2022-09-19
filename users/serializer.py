from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'password', 'token')
        extra_kwargs = {
            'password': {
                'validators': [validate_password],
                'style': {'input_type': 'password'}
            },

        }

    def get_token(self, user):
        token, created = Token.objects.get_or_create(user=user)
        return token.key
