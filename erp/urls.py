from django.urls import path
from erp.views import cria_funcionario, home

app_name = "erp"

urlpatterns = [
    path("", home),
    path("funcionarios/novo", cria_funcionario),
]
