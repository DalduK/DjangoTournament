# import form class from django
from django import forms

# import GeeksModel from models.py
from django.core.exceptions import ValidationError

from .models import Tournament, Player, Score


class DateInput(forms.DateInput):
    input_type = 'date'

# create a ModelForm
class TournamentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Tournament
        fields = ["name", "size"]

    def __init__(self, user, *args, **kwargs):
        self.createdBy = user
        super(TournamentForm, self).__init__(*args, **kwargs)


class TournamentConfirm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Tournament
        fields = ["closeDate"]
        widgets = {
            'closeDate': DateInput(),
        }


class PlayerForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Player
        fields = ('player_name',)


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('player1_score', 'player2_score',)

    def clean(self):
        form_data = self.cleaned_data
        if form_data["player1_score"] == form_data["player2_score"]:
            self._errors["player1_score"] = ["Draw is not an option, we have to fight for life."]
            del form_data["player1_score"]
        return form_data
