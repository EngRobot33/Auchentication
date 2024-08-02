from django.contrib.auth.models import AbstractUser

from apps.api.fields import PhoneNumberField


class User(AbstractUser):
    phone_number = PhoneNumberField()

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.phone_number
