from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from consultas.forms import ConsultaForm, ProcedimentoForm
from consultas.models import Consulta, Procedimento
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.db.models import Sum

# Create your views here.
#def consultas(request):
    #return render(request,'consultas.html')

class ConsultaListView(GroupRequiredMixin,LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionarios",]
    model = Consulta
    template_name = 'consultas.html'
    context_object_name = 'consultas'
    ordering = ['data']
    paginate_by = 10

class ConsultaListViewPacientes(GroupRequiredMixin,LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Pacientes",]
    model = Consulta
    template_name = 'listar_consultas_pacientes.html'
    context_object_name = 'consultasPacientes'
    ordering = ['data']
    paginate_by = 10
    def get_queryset(self):
        return Consulta.objects.filter(paciente=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consultas = Consulta.objects.filter(paciente=self.request.user)
        total_gasto = consultas.aggregate(Sum('procedimento__preco'))['procedimento__preco__sum']
        context['total_gasto'] = total_gasto
        return context
  
class ConsultaCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Pacientes"
    model = Consulta
    form_class = ConsultaForm
    template_name = 'criar_consulta.html'
    success_url = reverse_lazy('listar_consultas_pacientes')

    def form_valid(self, form):
        form.instance.paciente = self.request.user
        data = form.cleaned_data['data']
        horario = form.cleaned_data['horario']
        # Checa se há consultas agendadas para o mesmo horário e data
        consulta_existente = Consulta.objects.filter(data=data, horario=horario).exists()
        if consulta_existente:
            form.add_error(None, 'Já existe uma consulta agendada para este horário.')
            return self.form_invalid(form)
        return super().form_valid(form)
    
class EditarConsulta(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    group_required =  u"Pacientes"
    model = Consulta
    form_class = ConsultaForm
    template_name = 'editar_consulta.html'
    success_url = reverse_lazy('listar_consultas')

class ExcluirConsulta(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    group_required =  u"Pacientes"
    login_url = reverse_lazy('login')
    model = Consulta
    template_name = 'excluir_consulta.html'
    success_url = reverse_lazy('listar_consultas')

class CadastrarProcedimento(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionarios",]
    model = Procedimento
    form_class = ProcedimentoForm
    template_name = 'cadastrar_procedimento.html'
    success_url = reverse_lazy('listar_procedimentos')

class EditarProcedimento(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionarios",]
    model = Procedimento
    form_class = ProcedimentoForm
    template_name = 'editar_procedimento.html'
    success_url = reverse_lazy('listar_procedimentos')

class ExcluirProcedimento(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionarios",]
    model = Procedimento
    template_name = 'excluir_procedimento.html'
    success_url = reverse_lazy('listar_procedimentos')

class ListarProcedimentos(GroupRequiredMixin,LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Funcionarios",]
    model = Procedimento
    template_name = 'listar_procedimentos.html'
    context_object_name = 'procedimentos'
    ordering = ['nome_procedimento']
    paginate_by = 10
