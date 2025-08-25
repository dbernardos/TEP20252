from django.shortcuts import render, redirect
from .models import Produto
from django.http.response import HttpResponse

def index(request):
    context = {
        'texto': "Olá mundo!",
    }
    return render(request, 'index.html', context)

def produto(request):
    produtos = Produto.objects.all()
    # produtos = get_objects_or_404()
    context = {
        'produtos': produtos,
    }
    return render(request, 'produto.html', context)

def cad_produto(request):

    if request.method == "GET":
        return render(request, 'cad_produto.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        preco = request.POST.get('preco').replace(',', '.')
        qtde = request.POST.get('qtde')

        produto  = Produto(
            nome = nome,
            preco = preco,
            qtde = qtde,
        )
        produto.save()
        return redirect('url_produto')
