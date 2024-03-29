# coding: utf-8
import json
from django.http.response import HttpResponse,HttpResponseRedirect, JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from Alcooloria.core.service import cervejada_svc
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import log_svc
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from core.models import Metricas, Cerveja



def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        print('entrou')
        if user.is_active:
            print('entrou dois')
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated():
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


@require_POST
def cadastro(request):
    username=request.POST['username']
    email=request.POST['email']
    senha=request.POST['senha']
    novo_usuario = User.objects.create_user(username=username, email=email, password=senha)
    novo_usuario.save()
    return JsonResponse({})


def calculo(request):
    metrica = Metricas.objects.get(user=request.user)
    calorias = int(request.GET['qntd_cerveja']) * 150 
    velocidade = 13 if metrica.gender == "Masculino" else 11
    calculo = velocidade * metrica.weight * 0.0175
    tempo_corrida = calorias / calculo
    return JsonResponse(round(tempo_corrida), safe=False)
    
def metricas(request):
    user=request.POST['usuario']
    user=User.objects.get(id=user)
    height=request.POST['height']
    weight=request.POST['weight']
    gender=request.POST['gender']
    exercise=request.POST['exercise']
    metricas_user = Metricas.objects.create(user=user,height=height,weight=weight,gender=gender,exercise=exercise)
    metricas_user.save()
    return JsonResponse({})


def cadastra_cerveja(request):
    marca = request.POST['marca']
    mls = request.POST['mls']
    valor_calorico = request.POST['valor_calorico']
    cerveja = Cerveja.objects.create(marca=marca,mls=mls,valor_calorico=valor_calorico)
    cerveja.save()
    return JsonResponse({})


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated() else {'authenticated': False}
    return JsonResponse(i_am)


@ajax_login_required
def add_cervejada(request):
    cervejada = cervejada_svc.add_cervejada(request.POST['new_cervejada'])
    return JsonResponse(cervejada)


@csrf_exempt
@ajax_login_required
def delete_cervejada(request):
    id = request.POST["id"]
    cervejada_svc.delete_cervejada(id)
    return JsonResponse({})


@ajax_login_required
def list_cervejadas(request):
    cervejadas = cervejada_svc.list_cervejadas()
    return JsonResponse({'cervejadas': cervejadas})


def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d
