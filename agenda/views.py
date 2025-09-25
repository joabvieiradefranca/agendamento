#from django.shortcuts import render

# Create your views here.
'''from django.shortcuts import render
from django.utils.timezone import now
from .models import Agendamento

def dashboard(request):
    hoje = now().date()
    agendamentos_hoje = Agendamento.objects.filter(data=hoje)

    context = {
        "total_agendamentos_hoje": agendamentos_hoje.count(),
        "agendamentos": Agendamento.objects.all().order_by("data", "hora")
    }
    return render(request, "agenda/dashboard.html", context)'''

from django.shortcuts import render

def dashboard(request):
    return render(request, 'agenda/dashboard.html')
