from django.core import validators
from django.db import models

from apps.api.validators import IranianPhoneNumberValidator


class PhoneNumberField(models.CharField):
    def __init__(self, *args, db_collation=None, **kwargs):
        super(PhoneNumberField, self).__init__(*args, **kwargs)
        self.db_collation = db_collation
        self.verbose_name = "phone number"
        self._unique = True
        self.max_length = 13
        self.validators.append(IranianPhoneNumberValidator())

    def to_python(self, value):
        value = super(PhoneNumberField, self).to_python(value)
        if value and value.startswith('+98'):
            value = '0' + value[3:]
        elif value.startswith('98'):
            value = '0' + value[2:]
        return value
