# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Tournament, Player


# create a ModelForm
class TournamentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Tournament
        fields = ["name",  "size"]


    def __init__(self, user, *args, **kwargs):
        self.createdBy = user
        super(TournamentForm, self).__init__(*args, **kwargs)

class TournamentConfirm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Tournament
        fields = ["closeDate"]


class PlayerForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Player
        fields = ('player_name',)