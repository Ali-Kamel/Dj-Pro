from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default='')

    firstname = models.CharField(max_length=40, default='')

    lastname = models.CharField(max_length=40, default='')

    email = models.EmailField(max_length=100, default='')

    password = models.CharField(max_length=30)

    birthday = models.DateField()

    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
                              default='M',
                              )

    def __str__(self):
        return self.firstname