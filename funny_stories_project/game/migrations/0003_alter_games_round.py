# Generated by Django 5.0.6 on 2024-06-18 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_games_round_alter_games_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='round',
            field=models.IntegerField(default=1),
        ),
    ]