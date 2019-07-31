import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.models import BaseUserManager


# Create manager here


class UserProfileManager(BaseUserManager):
    """

    Helps django work with custom user models

    """

    def create_user(self, email, first_name, last_name, password):
        """
        Creates new user profile object
        :param last_name:
        :param first_name:
        :param email:
        :param password:
        :return:
        """

        if not email:
            raise ValueError('Provide an email address for user.')

        email = self.normalize_email(email)

        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates and saves a new superuser with given details
        :param last_name:
        :param first_name:
        :param email:
        :param password:
        :return:
        """

        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self.db)

        return user


# Create your models here.


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """

    Representing the user profile

    """
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        """
        Used to get user's  full name
        :return:

        """

        return self.first_name + self.last_name

    def get_short_name(self):
        """
        Used to get user's  short name
        :return:

        """

        return self.first_name

    def __str__(self):
        """
        Used to convert object to a string

        :return:
        """

        return self.email


class Plant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, blank=False, unique=True)

    def __str__(self):
        return self.name


class Datapoint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE)
    energy_expected = models.FloatField()
    energy_observed = models.FloatField()
    irradiation_expected = models.FloatField()
    irradiation_observed = models.FloatField()
