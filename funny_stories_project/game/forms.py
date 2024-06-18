from django import forms
from .models import Users
from datetime import datetime


class GameForm(forms.Form):
    """ Форма для добавления текста игры """
    text = forms.CharField(label='',
                           help_text='Напишите не меньше 2 слов',
                           widget=forms.Textarea(attrs={'type': 'text'}))

    def clean_text(self):
        """ Проверка на количество вводимых слов.
        Если слов меньше 2, то добавляем два '?' """
        text: str = self.cleaned_data['text']
        if len(text.split()) < 2:
            text += ' ? ?'
        return text


class GameSettingsForm(forms.Form):
    """ Форма для настроек игры """
    time = forms.CharField(initial=datetime.now()) # потом нужно удалить

    title = forms.CharField(label='Название истории',
                            initial='Новая история!',
                            widget=forms.TextInput())
    number_of_round = forms.IntegerField(label='Количество кругов',
                                         min_value=1,
                                         initial=1,
                                         widget=forms.NumberInput())
    players = forms.ChoiceField(label='Выберите игроков',
                                error_messages={"required": "Пожалуйста выберите игроков!"
                                                            "Количество игроков должно быть не менее 2."
                                                            "Если вашего игрока нет в предложенном списке, "
                                                            "вы можете добавить его в базу воспользовавшись "
                                                            "'Добавить нового игрока.'"},
                                choices=[(a.id, a.name) for a in Users.objects.all()],
                                initial='None',
                                required=True)


class NewUserForms(forms.Form):
    """Форма для добавления нового пользователя"""
    name = forms.CharField(label='Имя',
                           initial='Player',
                           max_length=50,
                           widget=forms.TextInput(attrs={
                               'placeholder': 'Введите имя пользователя',
                           }))
    age = forms.IntegerField(label='Возраст',
                             widget=forms.NumberInput())
    email = forms.EmailField(label='Почта',
                             initial='kuku@gmail.corporat',
                             widget=forms.EmailInput(attrs={
                                 'placeholder': 'user@mail.ru'
                             }))

    def clean_name(self):
        """ Проверка на наличие имени в базе данных """
        name: str = self.cleaned_data['name']
        if name in Users.objects.all().values_list('name', flat=True):
            raise forms.ValidationError('Такой игрока уже существует, пожалуйста введите другое имя')
        return name


