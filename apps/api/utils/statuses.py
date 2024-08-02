from rest_framework.views import status

# 200
OK_200 = {
    'detail': 'OK',
    'code': 'OK',
    'number': status.HTTP_200_OK
}

# 201
CREATED_201 = {
    'detail': 'Created',
    'code': 'created',
    'number': status.HTTP_201_CREATED
}

# 400
BAD_REQUEST_400 = {
    'detail': 'Bad request',
    'code': 'bad_request',
    'number': status.HTTP_400_BAD_REQUEST
}
OTP_EXPIRED_400 = {
    'detail': 'Otp expired',
    'code': 'otp_expired',
    'number': status.HTTP_400_BAD_REQUEST
}

EXPIRED_400 = {
    'detail': 'Expired',
    'code': 'expired',
    'number': status.HTTP_400_BAD_REQUEST
}

# 401
UNAUTHORIZED_401 = {
    'detail': 'Forbidden',
    'code': 'forbidden',
    'number': status.HTTP_401_UNAUTHORIZED
}
# 403
FORBIDDEN_403 = {
    'detail': 'Forbidden',
    'code': 'forbidden',
    'number': status.HTTP_403_FORBIDDEN
}
LOGIN_FAILED_403 = {
    'detail': 'Login failed',
    'code': 'login_failed',
    'number': status.HTTP_403_FORBIDDEN
}

# 404
NOT_FOUND_404 = {
    'detail': 'Not found',
    'code': 'not_found',
    'number': status.HTTP_404_NOT_FOUND
}
USER_NOT_FOUND_404 = {
    'detail': 'User not found',
    'code': 'user_not_found',
    'number': status.HTTP_404_NOT_FOUND
}

# 409
CONFLICT_409 = {
    'detail': 'Conflict',
    'code': 'conflict',
    'number': status.HTTP_409_CONFLICT
}

# 500
SERVER_ERROR_500 = {
    'detail': 'Server error',
    'code': 'server_error',
    'number': status.HTTP_500_INTERNAL_SERVER_ERROR
}

# 501
NOT_IMPLEMENTED_501 = {
    "detail": "Not Implemented",
    "code": "not_implemented",
    'number': status.HTTP_501_NOT_IMPLEMENTED

}

# 503
MAINTENANCE_MODE_503 = {
    "detail": "Match maintenance mode. Try again later...",
    'code': 'match_maintenance_mode',
    'number': status.HTTP_503_SERVICE_UNAVAILABLE
}
