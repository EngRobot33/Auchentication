import re

from django.core.exceptions import ValidationError


def iranian_phone_number_validator(value):
    """
    Checks if the provided phone number matches the Iranian phone number format.
    """
    iranian_pattern = re.compile(r'^(0|\+98)9\d{9}$')

    if not iranian_pattern.match(value):
        raise ValidationError('Phone number must be an Iranian phone number.')

    # Convert +98 to 0
    if value.startswith('+98'):
        value = '0' + value[3:]

    return value
