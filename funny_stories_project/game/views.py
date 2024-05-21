import logging
from django.shortcuts import render
from .forms import GameSettingsForm
from .forms import NewUserForms
from .models import User

logger = logging.getLogger(__name__)
LIST_USERS = []


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
            user = User(name=name, age=age, email=email)
            user.save()
            message = 'Игрок сохранен, добавить еще одного игрока?'
            return render(request, 'game/newuser.html', {'form': form, 'message': message})
    else:
        form = NewUserForms()
        LIST_USERS = []
        message = 'Заполните форму игрока'
    return render(request, 'game/newuser.html', {'form': form, 'message': message})


def game_settings(request):
    message = 'Заполните поля для создания игры!'
    if request.method == 'POST':
        form = GameSettingsForm(request.POST)
        if form.is_valid():
            # count_players = form.cleaned_data['count_players']
            word_count = form.cleaned_data['word_count']
            number_of_round = form.cleaned_data['number_of_round']
            player = User.objects.get(id=form.cleaned_data['players']).name
            LIST_USERS.append(player)
            players = ', '.join(LIST_USERS)
            logger.info(f'Выбранные игроки {LIST_USERS = }')
            logger.info('Game_settings ok valid')
            return render(request, 'game/game_settings.html', {'form': form, 'players': players, 'message': message})
    else:
        form = GameSettingsForm()
    return render(request, 'game/game_settings.html', {'form': form, 'message': message})
