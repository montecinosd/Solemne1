from django.shortcuts import render
from basket.models import *
from django.http import HttpResponse
from basket.forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url='/auth/login')
def index(request):
    data = {}

    # SELECT * FROM player
    object_list = Player.objects.all().order_by('-id')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'player/list_player.html'
    return render(request, template_name, data)

def TemplateAdd(request):
    template = 'add.html'
    data = {}
    if request.method == "POST":
        data['form'] = PlayerForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('player_list')

    else:
        data['form'] = PlayerForm()

    template_name = 'add.html'
    return render(request, template_name, data)

def delete_player(request,id_player):
    player = Player.objects.get(id=id_player)

    player.delete()
    return redirect('../list')
    return render(request,'delete.html', {'player':player})

def edit_player(request,id_player):
    player = Player.objects.get(id=id_player)
    if request.method == 'GET':
        form = PlayerForm(instance=player)
    else:
        form = PlayerForm(request.POST,instance=player)
        if form.is_valid():
            form.save()
        return redirect('../list')
    return render(request,'add.html',{'form':form})


def TemplateList(request):
    template = 'list.html'
    data = {}

    # SELECT * FROM player
    data['object_list'] = Player.objects.all()
    return render(request, template, data)

'''
Team
'''
#ADD TEAM
def TemplateAddTeam(request):
    template = 'addTeam.html'
    data = {}
    if request.method == "POST":
        data['form'] = TeamForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()
            return redirect('TemplatelistTeam')

    else:
        data['form'] = TeamForm()

    template_name = 'addTeam.html'
    return render(request, template_name, data)
#EDIT TEAM
def EditTeam(request,id_team):
    team = Team.objects.get(code=id_team)
    if request.method == 'GET':
        form = TeamForm(instance=team)
    else:
        form = TeamForm(request.POST,instance=team)
        if form.is_valid():
            form.save()
        return redirect('../listTeam')
    return render(request,'addTeam.html',{'form':form})

#LIST TEAM
def TemplateListTeam(request):
    template = 'listTeam.html'
    data = {}

    # SELECT * FROM player
    data['object_list'] = Team.objects.all()
    return render(request, template, data)
#DELETE TEAM
def DeleteTeam(request,id_team):
    team = Team.objects.get(code=id_team)

    team.delete()
    return redirect('../listTeam')
    return render(request,'deleteTeam.html', {'team':team})

def teamindex(request):
    data = {}

    data['saludar'] = 'Hola dsfs'

    # SELECT * FROM player
    data['object_list'] = Team.objects.all()

    template_name = 'player/list_player.html'
    return render(request, template_name, data)

'''
Coach
'''
#ADD COACH
def TemplateAddCoach(request):
    template = 'addCoach.html'
    data = {}
    if request.method == "POST":
        data['form'] = CoachForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()
            return redirect('TemplatelistCoach')

    else:
        data['form'] = CoachForm()

    template_name = 'addCoach.html'
    return render(request, template_name, data)

#
def TemplateListCoach(request):
    template = 'listCoach.html'
    data = {}

    # SELECT * FROM player
    data['object_list'] = Coach.objects.all()
    return render(request, template, data)

#EDIT COACH
def EditCoach(request,id_coach):
    coach = Coach.objects.get(id=id_coach)
    if request.method == 'GET':
        form = CoachForm(instance=coach)
    else:
        form = CoachForm(request.POST,instance=coach)
        if form.is_valid():
            form.save()
        return redirect('../listCoach')
    return render(request,'addCoach.html',{'form':form})

#DELETE COACH
def DeleteCoach(request,id_coach):
    coach = Coach.objects.get(id=id_coach)

    coach.delete()
    return redirect('../listCoach')
    return render(request,'deleteCoach.html', {'team':team})

def detail(request, player_id):

    data = {}
    template_name = 'player/detail_player.html'

    # SELECT * FROM player WHERE id = player_id
    data['player'] = Player.objects.get(pk=player_id)
    # import pdb;pdb.set_trace()
    print(data)
    return render(request, template_name, data)
