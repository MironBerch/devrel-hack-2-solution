from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Manager for `User` model."""

    def create_user(self, email: str, first_name: str, last_name: str, password: str = None):
        if not email:
            raise ValueError('Пользователи должны иметь адрес электронной почты.')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email: str, first_name: str, last_name: str, password: str):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, first_name: str, last_name: str, password: str):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
