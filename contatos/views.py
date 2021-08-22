from django.shortcuts import render, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.contrib import messages
from django.db.models.functions import Concat
# Create your views here.


def index(request):
    contatos = Contato.objects.filter(mostrar=True)
    per_p = 5
    paginator = Paginator(contatos, per_p)
    p_num = request.GET.get('p')
    contatos = paginator.get_page(p_num)
    return render(request, 'contatos/index.html', {'contatos': contatos})


def ver_contato(request, contato_id):
    contato = Contato.objects.get(id=contato_id)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR,
                             'O campo de busca não pode ser vazio!')
        return redirect('index')
    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(nome_completo=campos).filter(Q(nome__icontains=termo) | Q(
        sobrenome__icontains=termo) | Q(telefone__icontains=termo)).filter(mostrar=True)
    if contatos is None or not contatos:
        messages.add_message(request, messages.ERROR,
                             'Nenhum resultado encontrado')
        return redirect('index')
    per_p = 5
    paginator = Paginator(contatos, per_p)
    p_num = request.GET.get('p')
    contatos = paginator.get_page(p_num)
    return render(request, 'contatos/busca.html', {'contatos': contatos})
