from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse

from apps.api.response import custom_response
from apps.api.statuses import OTP_EXPIRED_400, CREATED_201, UNAUTHORIZED_401, LOGIN_FAILED_403, OK_200
from apps.api.utils import otp_send, otp_check, generate_token
from apps.api.views import BaseAPIView
from apps.user.api.serializers import PhoneNumberSerializer, OtpVerifySerializer, UserRegisterSerializer, \
    UserSerializer, UserLoginSerializer

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
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer, validated_data = self.data_validation()
        phone_number = validated_data['phone_number']

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return custom_response(status_code=LOGIN_FAILED_403)

        if not user.check_password(validated_data['password']):
            return custom_response(status_code=LOGIN_FAILED_403)

        return custom_response(data=UserSerializer(user).data, status_code=OK_200)


class UserRegisterApi(BaseAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer, validated_data = self.data_validation()

        if not self.request.auth:
            return custom_response(status_code=UNAUTHORIZED_401)

        user = self.request.user
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.email = validated_data['email']
        user.set_password(validated_data['password'])

        user.save(update_fields=['first_name', 'last_name', 'email', 'password'])

        return custom_response(data=UserSerializer(user).data, status_code=CREATED_201)
