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


def get_cache_key(ip_address, suffix):
    """
    Generate a unique cache key using the IP address and a suffix.
    """
    return f"{settings.CACHE_KEY_PREFIX}:{ip_address}:{suffix}"


def increment_attempts(ip_address, suffix):
    """
    Increment the number of failed attempts for the given IP address and action, and return the updated count.
    """
    cache_key = get_cache_key(ip_address, suffix)
    attempts = cache.get(cache_key, 0) + 1
    cache.set(cache_key, attempts, settings.BLOCK_DURATION)
    return attempts


def is_blocked(ip_address, suffix):
    """
    Check if the given IP address is blocked for the specified action based on the cache.
    """
    cache_key = get_cache_key(ip_address, suffix)
    return cache.get(cache_key) and cache.ttl(cache_key) > 0


def block_ip(ip_address, suffix):
    """
     Block the given IP address for the specified action by setting the cache to the attempt limit.
     """
    cache_key = get_cache_key(ip_address, suffix)
    cache.set(cache_key, settings.LOGIN_ATTEMPT_LIMIT, settings.BLOCK_DURATION)
