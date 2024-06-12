import logging
from django.shortcuts import render
from .forms import GameSettingsForm
from .forms import NewUserForms
from .forms import GameForm
from .models import User
from .models import Games
from django.views.decorators.cache import never_cache  # для полного отключения кеширования


logger = logging.getLogger(__name__)
LIST_USERS = []
# STORY = []


def home(request):
    global LIST_USERS
    LIST_USERS = []
    return render(request, 'game/home.html')


def new_user(request):
    """Function of adding new players to the database"""
    if request.method == 'POST':
        form = NewUserForms(request.POST)
        message = 'Ошибка данных'
        if form.is_valid():
            logger.info(f'{form.cleaned_data["name"] = }\n{User.objects.all().values_list("name") = }')
            user = User(name=form.cleaned_data['name'],
                        age=form.cleaned_data['age'],
                        email=form.cleaned_data['email'])
            user.save()
            message = 'Игрок сохранен, добавить еще одного игрока?'
            return render(request, 'game/newuser.html', {'form': form, 'message': message})
    else:
        message = 'Заполните форму игрока'
        form = NewUserForms()
    return render(request, 'game/newuser.html', {'form': form, 'message': message})


def game_settings(request):
    """Function to add the necessary parameters to start the game"""
    message = 'Заполните поля для создания игры!'
    playres = User.objects.all()
    if request.method == 'POST':
        form = GameSettingsForm(request.POST)
        if form.is_valid():
            logger.info('Game_settings ok valid')
            title_story = form.cleaned_data['title']
            number_of_round = form.cleaned_data['number_of_round']
            player = playres.get(id=form.cleaned_data['players']).name
            create_game = Games(settings=[], story=[{'title': title_story}], status=False)
            logger.info(f'{player = }')
            if player not in LIST_USERS:
                LIST_USERS.append(player)
            else:
                message = 'Такой игрок уже добавлен! Выберите или добавьте нового игрока!'
                return render(request, 'game/game_settings.html', {'form': form, 'message': message})
            players = ', '.join(LIST_USERS)
            logger.info(f'Выбранные игроки {LIST_USERS = }')
            game = Games(title_story=title_story,
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
    last_game = Games.objects.last()
    title_story = last_game.title_story
    list_players = last_game.list_players.split()
    player_walks = last_game.player_walks
    round = last_game.round
    number_of_round = last_game.number_of_round
    message = f'Круг {round}, ход игрока {list_players[player_walks]}'
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            logger.info('GameForm ok valid')
            story = form.cleaned_data['text']

            if number_of_round < round:
                logger.info(f'Сработал number_of_round < round: {number_of_round = }, {round = }')
                last_game.status = 'finish'
                message = 'Результат Ваших стараний!'
                return render(request, 'game/result.html', {'message': message,
                                                            'title_story': title_story,
                                                            'story': last_game.story,
                                                            })
            else:
                player_walks += 1
                if player_walks == len(list_players):
                    logger.info(f'Сработал player_walks == len(list_players): {player_walks = }, {len(list_players) = }')
                    round += 1
                    last_game.round += round
                    player_walks = 0
                    last_game.player_walks = player_walks
                else:
                    last_game.player_walks += 1
                last_game.story.append(story)
                last_game.status = 'game'
                logger.info(f'\n{title_story = }, \n{list_players = }, \n{last_game.story = }, \n{player_walks = }')
                last_game.save()
                message = f'Круг {round}, ход игрока {list_players[player_walks]}'
                form = GameForm()
                return render(request, 'game/game.html', {'form': form,
                                                          'title_story': title_story,
                                                          'message': message,
                                                          })
    else:
        form = GameForm()
    return render(request, 'game/game.html', {'form': form,
                                              'title_story': title_story,
                                              'message': message,
                                              })


def rules(request):
    """ Rules of the game """
    return render(request, 'game/rules.html')


def list_game(request):
    """ List of games """
    dict_game = [{'title_story': a.title_story,
                  'story': a.story,
                  'data': [a.data_game.date(), a.data_game.time()]} for a in Games.objects.all()]
    return render(request, 'game/list_game.html', {'dict_game': dict_game})
