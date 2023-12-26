from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
       Custom user model based on AbstractUser.

       Attributes:
        - email: Email field for user authentication.
        - username: Removed the username field.
        - USERNAME_FIELD: Set to 'email' for authentication.
        - REQUIRED_FIELDS: Empty list as no additional fields are required for user creation.

    """

    username = None

    email = models.EmailField(verbose_name=_('Email'), db_index=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'users'





