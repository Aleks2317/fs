from django import forms
from .models import User


# class GameForm(forms.Form):
#     game = forms.CharField(max_length=50)


class GameSettingsForm(forms.Form):
    count_players = forms.IntegerField(label='Количество игроков',
                                       min_value=2,
                                       max_value=10,
                                       initial=2,
                                       widget=forms.NumberInput(attrs={
                                           'class': 'form-control',
                                       }))
    word_count = forms.IntegerField(label='Минимальное количество слов',
                                    min_value=2,
                                    initial=2,
                                    widget=forms.NumberInput(attrs={
                                        'class': 'form-control',
                                    }))
    number_of_round = forms.IntegerField(label='Количество кругов',
                                         min_value=1,
                                         initial=1,
                                         widget=forms.NumberInput(attrs={
                                             'class': 'form-control',
                                         }))
    players = forms.ChoiceField(label='Выберите игроков',
                                error_messages={"required": "Пожалуйста выберите игроков!"
                                                            "Количество игроков должно быть не менее 2."
                                                            "Если вашего игрока нет в предложенном списке, "
                                                            "вы можете добавить его в базу воспользовавшись "
                                                            "'Добавить нового игрока.'"},
                                choices=[(a.id, a.name) for a in User.objects.all()],
                                initial='None')


class NewUserForms(forms.Form):
    name = forms.CharField(label='Имя',
                           initial='Player',
                           max_length=50,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Введите имя пользователя',
                           }))
    age = forms.IntegerField(label='Возраст',
                             min_value=14,
                             widget=forms.NumberInput(attrs={
                                 'class': 'form-control'
                             }))
    email = forms.EmailField(label='Почта',
                             initial='kuku@gmail.corporat',
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'user@mail.ru'
                             }))
#
#
# class RunGameForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     story = forms.CharField(max_length=1000)

