from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group 
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from usuarios.forms import EditarPacientesForm
from .forms import UsuarioForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request,'login.html')
@login_required(login_url='/login/') 
def listarPacientes(request):
    lista_pacientes = Group.objects.get(name='Pacientes')

    membros_pacientes = lista_pacientes.user_set.all()
    return render(request, 'pacientes.html', {'membros_pacientes': membros_pacientes})
@login_required(login_url='/login/') 
def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(User, id=paciente_id)
    form = EditarPacientesForm(instance=paciente)

    if request.method == 'POST':
        form = EditarPacientesForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')

    return render(request, 'editar_paciente.html', {'form': form, 'paciente': paciente})

@login_required(login_url='/login/') 
def excluir_paciente(request, paciente_id):
    paciente = get_object_or_404(User, id=paciente_id)
    paciente.delete()
    return redirect('listar_pacientes')

class UsuarioCreate(CreateView):
    template_name = "criar_conta.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Pacientes")
        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        return url
    
class UsuarioCreateFuncionario(CreateView):
    template_name = "criar_conta_funcionario.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Funcionarios")
        response = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        messages.success(self.request, 'Funcionário cadastrado com sucesso.')

        return response