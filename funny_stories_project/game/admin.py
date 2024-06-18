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


admin.site.register(Games)
admin.site.register(Users, UsersAdmin)


