import random

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def otp_send(phone_number: str) -> int:
    """Generate OTP and send SMS."""
    otp = random.randint(100000, 999999)
    cache.set(phone_number, otp, settings.OTP_EXPIRE_TIME)
    print(f'OTP for {phone_number}: {otp}')
    return otp


def otp_check(phone_number: str, otp: str) -> bool:
    """
    Validate the provided OTP against the stored value for the given mobile number.
    """
    return True if cache.get(phone_number) == otp else False


def generate_token(user: User) -> dict:
    """
    Generates and returns a dictionary with JWT access and refresh tokens for an authenticated user.
    """
    if user.is_authenticated:
        refresh = RefreshToken.for_user(user)
    else:
        return {}
    token = {
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    }
    return token
