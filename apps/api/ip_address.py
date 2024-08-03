from django.conf import settings

from django.core.cache import cache


class IPAddress:
    MAX_ATTEMPT_NUMBER: int = settings.MAX_ATTEMPT_NUMBER
    ATTEMPT_RESET_TIME: int = 10

    @staticmethod
    def get_ip_address(request):
        return request.META.get('REMOTE_ADDR')

    @classmethod
    def block_ip_address(cls, ip_address):
        cache.set(f"ip_blocked_{ip_address}", ip_address, cls.ATTEMPT_RESET_TIME)
        return True

    @classmethod
    def block_phone_number(cls, phone_number):
        cache.set(f"phone_number_blocked_{phone_number}", phone_number, cls.ATTEMPT_RESET_TIME)
        return True

    @classmethod
    def check_ip_is_blocked(cls, request):
        ip_address = cls.get_ip_address(request=request)
        return True if cache.get(f"ip_blocked_{ip_address}") else False

    @classmethod
    def attempt(cls, request=None, phone_number: str = None) -> bool:
        if request:
            ip_address = cls.get_ip_address(request=request)
            cache_value = cache.get(f"attempt_{ip_address}")
            value = cache_value + 1 if cache_value else 1
            if value > cls.MAX_ATTEMPT_NUMBER:
                cls.block_ip_address(ip_address=ip_address)
            else:
                cache.set(f"attempt_{ip_address}", value, cls.ATTEMPT_RESET_TIME)
        if phone_number:
            cache_value = cache.get(f"attempt_{phone_number}")
            value = cache_value + 1 if cache_value else 1
            if value > cls.MAX_ATTEMPT_NUMBER:
                cls.block_phone_number(phone_number=phone_number)
            else:
                cache.set(f"attempt_{phone_number}", value, cls.ATTEMPT_RESET_TIME)
        return True
