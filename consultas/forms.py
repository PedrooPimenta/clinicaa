import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Consulta, Procedimento

class ConsultaForm(forms.ModelForm):
    horario = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label='Horário')

    class Meta:
        model = Consulta
        fields = ['procedimento', 'data', 'horario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_data(self):
        data = self.cleaned_data['data']
        if data < datetime.date.today():
            raise ValidationError(_('Não é possível agendar uma consulta para uma data anterior à de hoje.'))
        return data

    def clean_horario(self):
        horario = self.cleaned_data['horario']
        if horario < datetime.time(8, 0) or horario > datetime.time(18, 0):
            raise ValidationError(_('O horário deve estar entre 08:00 e 18:00.'))
        return horario


class ProcedimentoForm(forms.ModelForm):
    class Meta:
        model = Procedimento
        fields = '__all__'