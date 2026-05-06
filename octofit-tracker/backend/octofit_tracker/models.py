# models.py
from django.db import models

# User model
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

# Team model
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    member_ids = models.JSONField(blank=True, default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Activity model
class Activity(models.Model):
    user_id = models.CharField(max_length=50)
    activity_type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(help_text='Durata in minuti')
    calories = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.activity_type}"

# Workout model
class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for_ids = models.JSONField(blank=True, default=list)

    def __str__(self):
        return self.name

# Leaderboard model
class Leaderboard(models.Model):
    user_id = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_id} - {self.score}"