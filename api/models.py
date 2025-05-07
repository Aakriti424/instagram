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

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Story(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    story=models.FileField(upload_to='story/')
    text=models.TextField()
    tag=models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags', null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user}'s story on {self.created_at}"


class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.FileField(upload_to='post/')
    text=models.TextField()
    tag=models.ForeignKey(User, on_delete=models.CASCADE, related_name='tagged', null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user}'s post on {self.created_at}"

class Friends(models.Model):
    STATUS_CHOICES=[
        ('friends', 'Friends'),
        ('pending', 'Pending'),
        ('reject','Reject')
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    friend=models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend', null=True, blank=True)
    status=models.CharField(max_length=60, choices=STATUS_CHOICES, default='pending')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s friend {self.friend}"
