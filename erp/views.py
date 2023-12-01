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
