import logging
from random import sample
from django.shortcuts import render
from .forms import GameSettingsForm
from .forms import NewUserForms
from .forms import GameForm
from .models import Users
from .models import Games


logger = logging.getLogger(__name__)
LIST_USERS = []


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
            logger.info(f'{form.cleaned_data["name"] = }\n{Users.objects.all().values_list("name") = }')
            user = Users(name=form.cleaned_data['name'],
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
    playres = Users.objects.all()
    if request.method == 'POST':
        form = GameSettingsForm(request.POST)
        if form.is_valid():
            logger.info('Game_settings ok valid')
            title_story = form.cleaned_data['title']
            number_of_round = form.cleaned_data['number_of_round']
            player = playres.get(id=form.cleaned_data['players']).name
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
    """Игра"""
    current_game = Games.objects.last()
    title_story = current_game.title_story
    list_players = current_game.list_players.split()
    player_walks = current_game.player_walks
    current_round = current_game.round
    number_of_round = current_game.number_of_round

    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            story = form.cleaned_data['text']
            player_walks += 1

            if player_walks == len(list_players):
                current_round += 1
                player_walks = 0
                logger.info(f'Новый круг {current_round = }')
            else:
                current_game.player_walks += 1

            current_game.player_walks = player_walks
            current_game.round = current_round
            current_game.story += f'&{story}'
            current_game.save()

            if number_of_round < current_round:
                logger.info(f'message_finish')
                current_game.status = True
                message_finish = 'Результат Ваших стараний!'
                return render(request, 'game/result.html', {'message': message_finish,
                                                            'title_story': title_story,
                                                            'story': current_game.story.split('&'),
                                                            })

            message_go = f'Круг {current_round}, ход игрока {list_players[player_walks]}'
            form = GameForm()
            return render(request, 'game/game.html', {'form': form,
                                                      'title_story': title_story,
                                                      'message': message_go,
                                                      'clue': ', '.join(sample(story.split(), 2))
                                                      })
    else:
        message = f"Круг {current_round}, ход игрока {list_players[player_walks]}"
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
                  'story': a.story.split('&'),
                  'data': [a.data_game.date(), a.data_game.time()]} for a in Games.objects.all()]
    return render(request, 'game/list_game.html', {'dict_game': dict_game})
