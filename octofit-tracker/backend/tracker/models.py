from django.db import models
from django.contrib.auth.models import AbstractUser
from bson import ObjectId

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.URLField(blank=True)

    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('run', 'Running'),
        ('cycle', 'Cycling'),
        ('swim', 'Swimming'),
        ('walk', 'Walking'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    description = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    distance = models.FloatField(blank=True, null=True, help_text='Distance in km')
    calories = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.description}"

    class Meta:
        ordering = ['-date', '-created_at']
