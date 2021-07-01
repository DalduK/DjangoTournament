# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Tournament


# create a ModelForm
class TournamentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Tournament
        fields = ["name", "closeDate", "size"]


    def __init__(self, user, *args, **kwargs):
        self.createdBy = user
        super(TournamentForm, self).__init__(*args, **kwargs)