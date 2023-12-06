from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from erp.forms import FormFuncionario
from erp.models import Funcionario


def home(request: HttpRequest):
    if request.method == "GET":
        return render(request, template_name="erp/index.html")


def cria_funcionario(request: HttpRequest):
    if request.method == "GET":
        form = FormFuncionario()

        return render(
            request,
            template_name="erp/funcionarios/new.html",
            context={"form": form},
        )
    elif request.method == "POST":
        form = FormFuncionario(request.POST)

        if form.is_valid():
            funcionario = Funcionario(**form.cleaned_data)

            funcionario.save()

            return HttpResponseRedirect(redirect_to="/")


def lista_funcionarios(request: HttpRequest):
    if request.method == "GET":
        funcionarios = Funcionario.objects.all()

        return render(
            request,
            template_name="erp/funcionarios/lista.html",
            context={"funcionarios": funcionarios},
        )


def busca_por_id(request: HttpRequest, pk: int):
    if request.method == "GET":
        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            funcionario = None

        return render(
            request,
            template_name="erp/funcionarios/detalhe.html",
            context={"funcionario": funcionario},
        )
