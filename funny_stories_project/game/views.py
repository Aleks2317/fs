import logging
from django.shortcuts import render
from .forms import GameForm


logger = logging.getLogger(__name__)


def home(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            logger.info(f'Получили {game=}')
            return render(request, 'game/home.html', {'form': form})
    else:
        form = GameForm()
    return render(request, 'game/home.html', {'form': form})