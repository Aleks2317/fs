from django.urls import path
from .views import home
from .views import game_settings
from .views import new_user


urlpatterns = [
    path('', home, name='home'),
    path('game_settings/', game_settings, name='game_settings'),
    path('newuser/', new_user, name='new_user'),

]
