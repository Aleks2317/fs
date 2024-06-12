from django.db import models


class Games(models.Model):
    """ Таблица игр """
    settings = models.JSONField(default=list)
    # title_story = models.CharField(max_length=150, default='')
    # list_players = models.TextField(default='')
    # player_walks = models.IntegerField(default=0)
    story = models.JSONField(default=list)
    # number_of_round = models.IntegerField(default=1)
    # round = models.IntegerField(default=1)
    data_game = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=None)

    def __str__(self):
        return f'Model is Games '


class SettingsGame(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    title_story = models.CharField(max_length=150, default='')
    list_players = models.TextField(default='')
    player_walks = models.IntegerField(default=0)
    number_of_round = models.IntegerField(default=1)
    round = models.IntegerField(default=1)
    status = models.CharField(max_length=15, default='')

    def __str__(self):
        return f'Model is SettingsGame'

    def get_settings(self):
        return f"[{self.title_story = }," \
               f"{self.list_players = }," \
               f"{self.player_walks = }," \
               f"{self.number_of_round = }," \
               f"{self.round = }," \
               f"{self.status = }]"


class Users(models.Model):
    """Таблица с игроками"""
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    email = models.EmailField(default='No email')
    data_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Model is User {self.name = }'




