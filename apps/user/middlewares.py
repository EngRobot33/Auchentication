from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from apps.api.ip_address import IPAddress


class IPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if IPAddress.check_ip_is_blocked(request=request):
            return JsonResponse(
                data=
                {
                    'detail': 'IP blocked',
                    'code': 403,
                    'data': {},
                    'error': None
                },
                status=403)
