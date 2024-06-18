from django.contrib import admin

from .models import Games, Users


class UsersAdmin(admin.ModelAdmin):
    """ Список игроков """
    # выбираем колнки которые мы хотим видеть
    list_display = ['name', 'age', 'data_registration']
    # Сортировка строк
    ordering = ['age', '-data_registration']
    # добавление фильтрации в список изменения
    list_filter = ['data_registration', 'name']
    search_fields = ['name']
    search_help_text = 'Поиск по полю name'


@admin.action(description="Поставить status = True")
def reset_status(modeladmin, request, queryset):
    queryset.update(status=True)


class GamesAdmin(admin.ModelAdmin):
    list_display = ['title_story', 'list_players', 'story', 'data_game', 'status']
    list_filter = ['status', 'data_game', 'title_story']
    ordering = ['-data_game']
    search_fields = ['title_story']
    search_help_text = 'Поиск по полю title_story'
    actions = [reset_status]


admin.site.register(Games, GamesAdmin)
admin.site.register(Users, UsersAdmin)


