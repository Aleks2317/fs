from django.db import models


class Games(models.Model):
    """ Таблица игр """
    title_story = models.CharField(max_length=150, default='')
    list_players = models.TextField(default='')
    story = models.TextField(default='')
    number_of_round = models.TextField(default='')
    data_game = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Model is Games {self.title_story = }'


class User(models.Model):
    """Таблица с игроками"""
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    email = models.EmailField(default='No email')
    data_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Model is User {self.name = }'




