from django.db import models


class User(models.Model):
    """Models - User."""
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    email = models.EmailField(default='No email')
    data_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Model is User {self.name = }'


class Games(models.Model):
    list_players = models.TextField()
    title = models.CharField(max_length=150)
    story = models.TextField()
    data_game = models.DateTimeField(auto_now_add=True)


