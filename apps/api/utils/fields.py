from django.core import validators
from django.db import models

from apps.api.utils.validators import iranian_phone_number_validator


class PhoneNumberField(models.CharField):
    def __init__(self, *args, db_collation=None, **kwargs):
        super(PhoneNumberField, self).__init__(*args, **kwargs)
        self.db_collation = db_collation
        self.verbose_name = "phone number"
        self._unique = True
        self.max_length = 13
        self.validators.append(validators.MaxLengthValidator(13))
        self.validators.append(iranian_phone_number_validator)

    def to_python(self, value):
        value = super(PhoneNumberField, self).to_python(value)
        if value and value.startswith('+98'):
            value = '0' + value[3:]
        return value
