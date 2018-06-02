from django.shortcuts import render
from basket.models import *
from django.http import HttpResponse
from basket.forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    data = {}

    # SELECT * FROM player
    object_list = Player.objects.all().order_by('-id')

    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = '../Template/list.html'
    return render(request, template_name, data)

@login_required(login_url='/auth/login')
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

@login_required(login_url='/auth/login')
def delete_player(request,id_player):
    player = Player.objects.get(id=id_player)

    player.delete()
    return redirect('../list')
    return render(request,'delete.html', {'player':player})

@login_required(login_url='/auth/login')
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

@login_required(login_url='/auth/login')
def TemplateList(request):
    template = 'list.html'
    data = {}
    object_list = Player.objects.all().order_by('-id')

    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    return render(request, template, data)

'''
Team
'''
#ADD TEAM
@login_required(login_url='/auth/login')
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
@login_required(login_url='/auth/login')
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
@login_required(login_url='/auth/login')
def TemplateListTeam(request):
    template = 'listTeam.html'
    data = {}
    object_list = Team.objects.all().order_by('-code')

    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    return render(request, template, data)
#DELETE TEAM
@login_required(login_url='/auth/login')
def DeleteTeam(request,id_team):
    team = Team.objects.get(code=id_team)

    team.delete()
    return redirect('../listTeam')
    return render(request,'deleteTeam.html', {'team':team})
@login_required(login_url='/auth/login')
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
@login_required(login_url='/auth/login')
def TemplateAddCoach(request):
    template = 'addCoach.html'
    data = {}
    if request.method == "POST":
        data['form'] = CoachForm(request.POST, request.FILES)
        data['form2'] = CreateCoachUserForm(request.POST, request.FILES)

        if data['form2'].is_valid():
            # aca el formulario valido
            aux = User.objects.create_user(username=request.POST["username"],
                            password= request.POST["password1"])
            aux.save()
        if data['form'].is_valid():
            # aca el formulario valido
            form = data['form'].save(commit=False)
            form= data['form'].save(commit=False)
            form.user = aux
            form.save()
            return redirect('TemplatelistCoach')


    else:
        data['form'] = CoachForm()
        data['form2'] = CreateCoachUserForm()

    template_name = 'addCoach.html'
    return render(request, template_name, data)

#
@login_required(login_url='/auth/login')
def TemplateListCoach(request):
    template = 'listCoach.html'
    data = {}
    object_list = Coach.objects.all().order_by('-id')

    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')

    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    return render(request, template, data)

#EDIT COACH
@login_required(login_url='/auth/login')
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
@login_required(login_url='/auth/login')
def DeleteCoach(request,id_coach):
    coach = Coach.objects.get(id=id_coach)

    coach.delete()
    return redirect('../listCoach')
    return render(request,'deleteCoach.html', {'team':team})
'''
Nomination
'''

#PUBLICA PARA QUE LOS JUGADORS PUEDAN VERLA
def TemplateListNomination(request):
    template = 'listNomination.html'
    data = {}

    # SELECT * FROM player
    data['object_list'] = Nomination.objects.all()

    #MOSTRAR STR LOS JUGADORES
    # aux_str= ''
    # for i in data['object_list']:
    #     a = i.player.all()
    #     a = list(a)
    #
    #     print (type(a))
    #     print (a)
    #     for x in a:
    #         print(list(a))

    return render(request, template, data)

@login_required(login_url='/auth/loginCoach')
def TemplateAddNomination(request):
    template = 'addNomination.html'
    data = {}
    if request.method == "POST":
        nomination = NominationForm(request.POST, request.FILES)
        data['form'] = nomination

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()
            return redirect('TemplateListNomination')

    else:
        nomination =NominationForm()
        data['form'] = NominationForm()

    template_name = 'addNomination.html'
    return render(request, template_name, data)

def detail(request, player_id):

    data = {}
    template_name = 'player/detail_player.html'

    # SELECT * FROM player WHERE id = player_id
    data['player'] = Player.objects.get(pk=player_id)
    # import pdb;pdb.set_trace()
    print(data)
    return render(request, template_name, data)
