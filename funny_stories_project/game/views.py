import logging
from django.shortcuts import render
from .forms import GameSettingsForm
from .forms import NewUserForms
from .forms import GameForm
from .models import User
from .models import Games

logger = logging.getLogger(__name__)
LIST_USERS = []
STORY = []


def home(request):
    global LIST_USERS, STORY
    LIST_USERS = []
    STORY = []
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
    """Function of adding new players to the database"""
    if request.method == 'POST':
        form = NewUserForms(request.POST)
        message = 'Ошибка данных'
        if form.is_valid():
            user = User(name=form.cleaned_data['name'],
                        age=form.cleaned_data['age'],
                        email=form.cleaned_data['email'])
            user.save()
            message = 'Игрок сохранен, добавить еще одного игрока?'
            return render(request, 'game/newuser.html', {'form': form, 'message': message})
    else:
        form = NewUserForms()
        message = 'Заполните форму игрока'
    return render(request, 'game/newuser.html', {'form': form, 'message': message})


def game_settings(request):
    """Function to add the necessary parameters to start the game"""
    message = 'Заполните поля для создания игры!'
    if request.method == 'POST':
        form = GameSettingsForm(request.POST)
        if form.is_valid():
            logger.info('Game_settings ok valid')
            number_of_round = form.cleaned_data['number_of_round']
            player = User.objects.get(id=form.cleaned_data['players']).name
            logger.info(f'{player = }')
            if player not in LIST_USERS:
                LIST_USERS.append(player)
            else:
                message = 'Такой игрок уже добавлен! Выберите или добавьте нового игрока!'
                return render(request, 'game/game_settings.html', {'form': form, 'message': message})
            players = ', '.join(LIST_USERS)
            logger.info(f'Выбранные игроки {LIST_USERS = }')
            game = Games(title_story=form.cleaned_data['title'],
                         list_players=players,
                         number_of_round=number_of_round,
                         )
            game.save()
            logger.info(f'Save - Game: {game = }')
            return render(request, 'game/game_settings.html', {'form': form, 'players': players, 'message': message})
    else:
        form = GameSettingsForm()
    return render(request, 'game/game_settings.html', {'form': form, 'message': message})


def game(request):
    """Game"""
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            logger.info('GameForm ok valid')
            STORY.append(form.cleaned_data['text'])
            last_game = Games.objects.last()
            last_game.story = ', '.join(STORY)
            last_game.save()
            logger.info(f'{Games.objects.last().story = }')
            form = GameForm()
            return render(request, 'game/game.html', {'form': form})
    else:
        form = GameForm()
    return render(request, 'game/game.html', {'form': form})


def rules(request):
    """ Rules of the game """
    return render(request, 'game/rules.html')
