import logging
from django.shortcuts import render
from .forms import GameSettingsForm
from .forms import NewUserForms
from .models import User

logger = logging.getLogger(__name__)


def home(request):
    # if request.method == 'POST':
    #     form = GameForm(request.POST)
    #     if form.is_valid():
    #         game = form.cleaned_data['game']
    #         logger.info(f'Получили {game=}')
    #         return render(request, 'game/home.html', {'form': form})
    # else:
    #     form = GameForm()
    return render(request, 'game/home.html')


def new_user(request):
    if request.method == 'POST':
        form = NewUserForms(request.POST)
        message = 'Ошибка данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            logger.info(f'Получили {name = }, {age = }, {email = }')
            player = User(name=name, age=age, email=email)
            player.save()
            message = 'Игрок сохранен, добавить еще одного игрока?'
            return render(request, 'game/newuser.html', {'form': form, 'message': message})
    else:
        form = NewUserForms()
        message = 'Заполните форму игрока'
    return render(request, 'game/newuser.html', {'form': form, 'message': message})


def game_settings(request):
    if request.method == 'POST':
        form = GameSettingsForm(request.POST)
        if form.is_valid():
            logger.info('Game_settings ok valid')
            return render(request, 'game/game_settings.html', {'form': form})
    else:
        form = GameSettingsForm()
    return render(request, 'game/game_settings.html', {'form': form})
