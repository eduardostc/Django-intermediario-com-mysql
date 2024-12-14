from django.shortcuts import render
from .forms import contatoForm
from django.contrib import messages


def index(request):
  return render(request, 'index.html')


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
   return render(request, 'produto.html')