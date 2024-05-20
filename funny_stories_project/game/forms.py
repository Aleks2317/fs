from django import forms
from .models import User


# class GameForm(forms.Form):
#     game = forms.CharField(max_length=50)


class GameSettingsForm(forms.Form):
    count_players = forms.IntegerField(min_value=2, max_value=10, widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))
    word_count = forms.IntegerField(min_value=5, widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))
    number_of_round = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))
    list_players = forms.ChoiceField(choices=[(a.id, a.name) for a in User.objects.all()])


class NewUserForms(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя пользователя'
    }))
    age = forms.IntegerField(min_value=18, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'user@mail.ru'
    }))
#
#
# class RunGameForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     story = forms.CharField(max_length=1000)

