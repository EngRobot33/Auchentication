import random


def otp_send() -> int:
    """Generate OTP and send SMS."""
    otp = random.randint(100000, 999999)
    print(otp)
    return otp
