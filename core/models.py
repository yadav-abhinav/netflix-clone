
from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

AGE_CHOICES=(
    ('all','All'),
    ('kids','Kids')
)

MOVIE_TYPES=(
    ('seasonal','Seasonal'),
    ('single','Single')
)

class CustomUser(AbstractUser):
    profiles=models.ManyToManyField('Profile',blank=True)

class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title=models.CharField(max_length=225)
    introduction=models.TextField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4)
    type=models.CharField(max_length=10,choices=MOVIE_TYPES)
    videos=models.ManyToManyField('Video')
    flyer=models.ImageField(upload_to='flyers')
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICES)
    def __str__(self):
        return self.title

class Video(models.Model):
    title=models.CharField(max_length=225,blank=True,null=True)
    file=models.FileField(upload_to='movies')
    def __str__(self):
        return self.title
