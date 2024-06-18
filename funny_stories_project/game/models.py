from django.db import models


class Games(models.Model):
    """ Таблица игр """
    title_story = models.CharField(max_length=150, default='')
    list_players = models.TextField()
    player_walks = models.IntegerField(default=0)
    story = models.TextField()
    number_of_round = models.IntegerField(default=1)
    round = models.IntegerField(default=1)
    data_game = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'Model is Games'


class Users(models.Model):
    """Таблица с игроками"""
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    email = models.EmailField(default='No email')
    data_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Model is User {self.name = }'




