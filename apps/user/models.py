from django.contrib.auth.models import AbstractUser

from apps.api.fields import PhoneNumberField
from apps.user.managers import UserManager


class User(AbstractUser):
    phone_number = PhoneNumberField()

    USERNAME_FIELD = 'phone_number'

    objects = UserManager()

    def __str__(self):
        return self.phone_number
