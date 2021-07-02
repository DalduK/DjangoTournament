from datetime import datetime

from django.db import models
from django.conf import settings

SIZE_CHOICES = (
    (4,4),
    (8,8),
    (16,16),
    (32,32),
    (64,64),
)


class Tournament(models.Model):
    createdBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
    )
    name = models.CharField(max_length=200)
    creatonDate = models.DateField(auto_now_add=True)
    closeDate = models.DateField(null=True)
    size = models.IntegerField(choices=SIZE_CHOICES, default='4')


class Player(models.Model):
    tournament = models.ForeignKey(Tournament,
        on_delete=models.CASCADE, null=False)
    player_name = models.CharField(max_length=200)


class BracketPair(models.Model):
    player1 = models.ForeignKey(Player,
        related_name='player_1',
        on_delete=models.CASCADE, null=False)
    player2 = models.ForeignKey(Player,
        on_delete=models.CASCADE,
        related_name='player_2',null=False)
    pairNumber = models.IntegerField(null=False)


class Score(models.Model):
    pair = models.ForeignKey(BracketPair,
        on_delete=models.CASCADE, null=False)
    player1_score = models.IntegerField(null=False)
    player2_score = models.IntegerField(null=False)
