from django.shortcuts import render
from basket.models import Player
from django.http import HttpResponse
from basket.forms import PlayerForm
from django.shortcuts import redirect


def index(request):
    data = {}

    data['saludar'] = 'Hola dsfs'

    # SELECT * FROM player
    data['object_list'] = Player.objects.all()

    template_name = 'player/list_player.html'
    return render(request, template_name, data)

def TemplateAgregar(request):
    template = 'agregar.html'
    data = {}
    if request.method == "POST":
        data['form'] = PlayerForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('player_list')

    else:
        data['form'] = PlayerForm()

    template_name = 'agregar.html'
    return render(request, template_name, data)


def editar_jugador(request,id_jugador):
    jugador = Player.objects.get(id=id_jugador)
    if request.method == 'GET':
        form = PlayerForm(instance=jugador)
    else:
        form = PlayerForm(request.POST,instance=jugador)
        if form.is_valid():
            form.save()
        return redirect('../listar')
    return render(request,'agregar.html',{'form':form})

def eliminar_jugador(request,id_jugador):
    jugador = Player.objects.get(id=id_jugador)

    jugador.delete()
    return redirect('../listar')
    return render(request,'eliminar.html', {'jugador':jugador})

def Templatelistar(request):
    template = 'listar.html'
    data = {}

    # SELECT * FROM player
    data['object_list'] = Player.objects.all()
    return render(request, template, data)

def detail(request, player_id):

    data = {}
    template_name = 'player/detail_player.html'

    # SELECT * FROM player WHERE id = player_id
    data['player'] = Player.objects.get(pk=player_id)
    # import pdb;pdb.set_trace()

    return render(request, template_name, data)
