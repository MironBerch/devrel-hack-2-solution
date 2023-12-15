from model_utils import FieldTracker
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractUser, Permission, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

from accounts.managers import UserManager


class User(AbstractUser, PermissionsMixin):
    """Custom user model."""

    username = None
    email = models.EmailField(
        verbose_name='email',
        max_length=60,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='имя',
        max_length=40,
    )
    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=40,
    )
    is_email_confirmed = models.BooleanField(
        verbose_name='электронная почта подтверждена',
        default=False,
    )
    date_joined = models.DateTimeField(
        verbose_name='дата присоединения',
        auto_now_add=True,
    )
    last_login = models.DateTimeField(
        verbose_name='последний вход',
        auto_now=True,
    )
    phone_number = PhoneNumberField(
        verbose_name='номер телефона',
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+?[0-9]{7,15}$',
                message='Номер телефона необходимо ввести в формате: +XXXXXXXXXXXXX.',
            )
        ]
    )
    is_active = models.BooleanField(
        verbose_name='активный',
        default=True,
    )
    is_staff = models.BooleanField(
        verbose_name='персонал',
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name='суперпользователь',
        default=False,
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    email_tracker = FieldTracker(fields=['email'])

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email

    def get_all_permissions(self, obj=None):
        if self.is_active and self.is_superuser:
            return Permission.objects.all()
        return Permission.objects.filter(user=self)

    def has_perm(self, perm, obj=None):
        if perm in self.get_all_permissions() or perm in self.get_group_permissions():
            return True
        return False

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
