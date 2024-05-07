from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views 
from .views import UsuarioCreate, UsuarioCreateFuncionario
urlpatterns = [
   # path('', view, name=""),
   path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('pacientes/', views.listarPacientes, name='listar_pacientes'),
   path('editar-paciente/<int:paciente_id>/', views.editar_paciente, name='editar_paciente'),
   path('excluir-paciente/<int:paciente_id>/', views.excluir_paciente, name='excluir_paciente'),
   path('registrar/', UsuarioCreate.as_view(), name='registrar'),
   path('registrar-funcionario/', UsuarioCreateFuncionario.as_view(), name='registrar_funcionario'),
]
