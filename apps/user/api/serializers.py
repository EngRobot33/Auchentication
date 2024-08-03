from rest_framework import serializers


class PhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)


class OtpVerifySerializer(PhoneNumberSerializer):
    otp = serializers.IntegerField()
