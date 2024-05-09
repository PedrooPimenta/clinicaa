from django.urls import path
from .views import ConsultaCreateView,ExcluirConsulta,ConsultaListView,EditarConsulta, ConsultaListViewPacientes, CadastrarProcedimento , EditarProcedimento, ExcluirProcedimento, ListarProcedimentos

urlpatterns = [
    path('consultas-clinica', ConsultaListView.as_view(), name='listar_consultas'),
    path('nova/', ConsultaCreateView.as_view(), name='criar_consultas'),
    path('excluir/<int:pk>/', ExcluirConsulta.as_view(), name='excluir_consultas'),
    path('editar/<int:pk>/', EditarConsulta.as_view(), name='editar_consultas'),
    path('consultas/', ConsultaListViewPacientes.as_view(), name='listar_consultas_pacientes'),
    path('procedimentos/', ListarProcedimentos.as_view(), name='listar_procedimentos'),
    path('novo-procedimento/', CadastrarProcedimento.as_view(), name='cadastrar_procedimento'),
    path('editar-procedimento/<int:pk>/', EditarProcedimento.as_view(), name='editar_procedimento'),
    path('excluir-procedimento/<int:pk>/', ExcluirProcedimento.as_view(), name='excluir_procedimento'),
]