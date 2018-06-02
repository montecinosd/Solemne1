from django.forms import ModelForm
from basket.models import Player, Team, Coach, Nomination
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
#

class CreateCoachUserForm(ModelForm):
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','password1', 'password2', )

class NominationForm(ModelForm):
    class Meta:
        model = Nomination
        # name_Math = forms.CharField(max_length=100)
        # player = forms.ModelMultipleChoiceField(queryset=Player.objects.all())
        fields = ['name_Match','date','hour','player','player','player']

#Funcionaba mal, la idea un checklist y que apretara los jugadores
# class NominationForm(forms.Form):
#     players = forms.ModelMultipleChoiceField(widget=forms.Select(attrs={'size':'13', 'onchange':'this.form.action=this.form.submit()'}), queryset=Player.objects.all().order_by('id'))
#     # name_Math = forms.CharField(max_length=100)
#     # player = forms.ModelMultipleChoiceField(queryset=Player.objects.all())
#     def __init__(self, *args, **kwargs):
#         super(NominationForm, self).__init__(*args, **kwargs)
#         name_Math = forms.CharField(max_length=100)
#         self.fields['players'].queryset = Player.objects.all()
