import math
import random
from .models import Player, BracketPair, Score


def pop_random(lst):
    idx = random.randrange(0, len(lst))
    return lst.pop(idx)


def load_table(id):
    print(id[0])
    players = Player.objects.filter(tournament=id[0])
    number = 1
    list_of_players = []
    list_of_size = []
    size = len(players)
    temp_size = int(size / 2)
    while temp_size != 0:
        list_of_size.append(temp_size)
        temp_size = int(temp_size / 2)
    list_of_size.pop(0)
    for i in players:
        list_of_players.append(i)
    while players:
        if len(list_of_players) > 0:
            player1 = pop_random(list_of_players)
            player2 = pop_random(list_of_players)
            pair = BracketPair(player1=player1, player2=player2, tournament=id[0], stage=int(size / 2),
                               pairNumber=number, open=True)
            pair.save()
            number += 1
        elif number < len(players):
            for i in list_of_size:
                for l in range(1, i + 1):
                    pair = BracketPair(player1=None, player2=None, tournament=id[0], stage=i, pairNumber=l, open=False)
                    pair.save()
                    number += 1
        else:
            break


def update_player_in_bracket(id):
    pair = BracketPair.objects.filter(id=id)
    score = Score.objects.filter(pair=pair[0].id)
    if score[0].player1_score > score[0].player2_score:
        if pair[0].pairNumber % 2 == 1 or pair[0].pairNumber == 1:
            number = int(math.ceil(pair[0].pairNumber / 2))
            update_pair = BracketPair.objects.filter(pairNumber=number, stage=int(pair[0].stage / 2),
                                                     tournament=pair[0].tournament.id)
            update_pair.update(player1=pair[0].player1)
            pair.update(open=False)
            if update_pair:
                if update_pair[0].player1 and update_pair[0].player2:
                    update_pair.update(open=True)
        else:
            number = int(pair[0].pairNumber / 2)
            update_pair = BracketPair.objects.filter(pairNumber=number, stage=int(pair[0].stage / 2),
                                                     tournament=pair[0].tournament.id)
            update_pair.update(player2=pair[0].player1)
            pair.update(open=False)
            if update_pair:
                if update_pair[0].player1 and update_pair[0].player2:
                    update_pair.update(open=True)
    else:
        if pair[0].pairNumber % 2 == 1 or pair[0].pairNumber == 1:
            number = int(math.ceil(pair[0].pairNumber / 2))
            update_pair = BracketPair.objects.filter(pairNumber=number, stage=int(pair[0].stage / 2),
                                                     tournament=pair[0].tournament.id)
            update_pair.update(player1=pair[0].player2)
            pair.update(open=False)
            if update_pair:
                if update_pair[0].player1 and update_pair[0].player2:
                    update_pair.update(open=True)
        else:
            number = int(pair[0].pairNumber / 2)
            update_pair = BracketPair.objects.filter(pairNumber=number, stage=int(pair[0].stage / 2),
                                                     tournament=pair[0].tournament.id)
            update_pair.update(player2=pair[0].player2)
            pair.update(open=False)
            if update_pair:
                if update_pair[0].player1 and update_pair[0].player2:
                    update_pair.update(open=True)
