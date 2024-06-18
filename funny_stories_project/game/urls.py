from django.urls import path
from .views import home
from .views import rules
from .views import game_settings
from .views import new_user
from .views import game
from .views import list_game


urlpatterns = [
    path('', home, name='home'),
    path('rules/', rules, name='rules'),
    path('game_settings/', game_settings, name='game_settings'),
    path('newuser/', new_user, name='new_user'),
    path('game/', game, name='game'),
    path('list_game/', list_game, name='list_game'),

]
