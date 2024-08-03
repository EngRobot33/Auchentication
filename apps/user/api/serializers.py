from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.api.utils import generate_token

User = get_user_model()


class PhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)


class OtpVerifySerializer(PhoneNumberSerializer):
    otp = serializers.IntegerField()


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'first_name', 'last_name', 'tokens']

    def get_tokens(self, obj):
        return generate_token(obj)
