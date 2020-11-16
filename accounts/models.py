from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import EmailValidator

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
            """Create and save a User with the given email and password."""
            if not email:
                raise ValueError('The given email must be set')
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        # extra_fields.setdefault('is_staff', False)
        # extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(validators=[EmailValidator], verbose_name='email', max_length=255, unique=True)
    age = models.IntegerField(null=True)
    hobby = models.CharField(max_length=50, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None

    objects = UserManager()


    # def get_username(self):
    #     return self.email