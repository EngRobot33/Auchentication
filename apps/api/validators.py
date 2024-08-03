from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class IranianPhoneNumberValidator(RegexValidator):
    regex = r'^(?:0|98|\+98)?(9\d{9})$'
    message = "Phone number must be an Iranian phone number."
    code = "invalid"

    def __init__(self, regex=None, message=None, code=None, inverse_match=None, flags=None):
        super().__init__(regex=self.regex, message=message, code=code, inverse_match=inverse_match, flags=flags)

    def __call__(self, value):
        super().__call__(value)

        # Convert +98 or 98 to 0
        if value.startswith('+98'):
            value = '0' + value[3:]
        elif value.startswith('98'):
            value = '0' + value[2:]

        return value
