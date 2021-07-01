# Generated by Django 3.2.4 on 2021-06-30 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BracketPair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pairNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('wins', models.IntegerField(default=0)),
                ('loses', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('creatonDate', models.DateField(auto_now_add=True)),
                ('isOpen', models.BooleanField()),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentPlayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.player')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1_score', models.IntegerField()),
                ('player2_score', models.IntegerField()),
                ('pair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.bracketpair')),
            ],
        ),
        migrations.AddField(
            model_name='bracketpair',
            name='player1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_1', to='tournament.player'),
        ),
        migrations.AddField(
            model_name='bracketpair',
            name='player2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_2', to='tournament.player'),
        ),
        migrations.AddField(
            model_name='bracketpair',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournament'),
        ),
    ]
