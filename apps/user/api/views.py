from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse

from apps.api.response import custom_response
from apps.api.utils import otp_send
from apps.api.views import BaseAPIView
from apps.user.api.serializers import PhoneNumberSerializer

User = get_user_model()


class UserCheckPhoneNumberApi(BaseAPIView):
    serializer_class = PhoneNumberSerializer

    def post(self, request):
        serializer, validated_data = self.data_validation()
        phone_number = validated_data['phone_number']
        is_exist = User.objects.filter(phone_number=phone_number).exists()

        if not is_exist:
            otp_send()
            return custom_response(data={'link': reverse('user:otp-verify')})

        return custom_response(data={'link': reverse('user:login')})


class UserOTPVerifyApi(BaseAPIView):
    ...


class UserLoginApi(BaseAPIView):
    ...


class UserRegisterApi(BaseAPIView):
    ...
