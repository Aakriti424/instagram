from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    GENDER_CHOICES=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ]
    email=models.EmailField(unique=True)
    mobile_number = models.IntegerField()
    full_name=models.CharField(max_length=300)
    gender=models.CharField(max_length=100, choices=GENDER_CHOICES)
    birth_date=models.DateField()

    bio=models.TextField(null=True, blank=True)
    profile_picture=models.ImageField(upload_to='profile/',null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

