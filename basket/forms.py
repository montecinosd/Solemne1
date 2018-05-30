from django.forms import ModelForm
from basket.models import Player, Team, Coach


class TeamForm(ModelForm):
    class Meta:
        model =Team
        fields = ['name','description','logo','code']

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['rut', 'dv', 'name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position', 'team']


class CoachForm(ModelForm):
    class Meta:
        model = Coach
        fields = ['name','age','email','nickname','rut','dv',]
