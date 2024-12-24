from django.shortcuts import render, redirect
from .forms import contatoForm, ProdutoModelForm
from django.contrib import messages

from .models import Produto

def index(request):
  context = {
     'produtos': Produto.objects.all()
  }
  return render(request, 'index.html', context)


def contato(request):
    form = contatoForm(request.POST or None)

    if str(request.method) == 'POST':
       if form.is_valid():
          form.send_mail()

          messages.success(request, 'E-mail enviado com sucesso')
          form = contatoForm()      
       else:
          messages.error(request, 'Erro ao enviar e-mail')
    context = {
       'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
   if str(request.method) != 'AnonymousUser':
      if str(request.method) == 'POST':
         form = ProdutoModelForm(request.POST, request.FILES)
         if form.is_valid():
            form.save()

            messages.success(request, 'Poduto salvo com sucesso.')
            form = ProdutoModelForm()
         else:
            messages.error(request, 'Erro ao salvar produto')
      else:
         form = ProdutoModelForm()

      context = {
         'form': form
      }

      return render(request, 'produto.html', context)
   else:
      return redirect('index')
      