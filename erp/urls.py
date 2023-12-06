from django.urls import path
from erp.views import busca_por_id, cria_funcionario, home, lista_funcionarios

app_name = "erp"

urlpatterns = [
    path("", home),
    path("funcionarios/", lista_funcionarios),
    path("funcionarios/novo", cria_funcionario),
    path("funcionarios/detalhe/<pk>", busca_por_id),
]
