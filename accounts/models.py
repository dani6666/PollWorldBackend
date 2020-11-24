from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator


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
    class PlaceOfResidence(models.IntegerChoices):
        VILLAGE = 1
        CITY = 2
        METROPOLIS = 3
    email = models.EmailField(validators=[EmailValidator], verbose_name='email', max_length=255, unique=True)
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    sex = models.BooleanField(null=True)
    profession = models.CharField(max_length=50, null=True)
    place_of_residence = models.IntegerField(choices=PlaceOfResidence.choices, null=True)
    growth = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    level_of_fitness = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None

    objects = UserManager()

    def to_json(self):
        return {
            'name': self.name,
            'age': self.age,
            'sex': self.sex,
            'profession': self.profession,
            'place_of_residence': self.place_of_residence,
            'growth': self.growth,
            'weight': self.weight,
            'level_of_fitness': self.level_of_fitness
        }
