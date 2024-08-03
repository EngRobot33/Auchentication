from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse

from apps.api.response import custom_response
from apps.api.statuses import OTP_EXPIRED_400, CREATED_201
from apps.api.utils import otp_send, otp_check, generate_token
from apps.api.views import BaseAPIView
from apps.user.api.serializers import PhoneNumberSerializer, OtpVerifySerializer

User = get_user_model()


class UserCheckPhoneNumberApi(BaseAPIView):
    serializer_class = PhoneNumberSerializer

    def post(self, request):
        serializer, validated_data = self.data_validation()
        phone_number = validated_data['phone_number']
        is_exist = User.objects.filter(phone_number=phone_number).exists()

        if not is_exist:
            otp_send(phone_number=phone_number)
            return custom_response(data={'link': reverse('user:otp-verify')})

        return custom_response(data={'link': reverse('user:login')})


class UserOTPVerifyApi(BaseAPIView):
    serializer_class = OtpVerifySerializer

    def post(self, request):
        serializer, validated_data = self.data_validation()
        phone_number = validated_data['phone_number']
        otp = validated_data['otp']
        if otp_check(phone_number=phone_number, otp=otp):
            user = User.objects.create(phone_number=phone_number, username=phone_number)
            data = {'link': reverse('user:register'), 'tokens': generate_token(user=user)}
            return custom_response(data=data, status_code=CREATED_201)
        return custom_response(status_code=OTP_EXPIRED_400)


class UserLoginApi(BaseAPIView):
    ...


class UserRegisterApi(BaseAPIView):
    ...
