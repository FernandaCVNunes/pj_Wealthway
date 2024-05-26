from django.shortcuts import render
from app_wealthway.models import Financas
from app_wealthway.forms import FinancasForm

def metas(request):
    if request.method == 'POST':
        form = FinancasForm(request.POST)

        if form.is_valid():
            financa = form.save(commit=False)
            financa.parcelas_totais = int(financa.valor_total / financa.valor_mensal)
            financa.save()
            return render(request, 'app_wealthway/templates/sucesso.html', {'parcelas': financa.parcelas_totais,'nome_meta':financa.nome_meta,'valor_total':financa.valor_total})
        else:
            lp_metas = Financas.objects.all()
            return render(request, 'app_wealthway/templates/base.html', {'form': form, 'lp_metas': lp_metas})

    else:
        form = FinancasForm()

        lp_metas = Financas.objects.all()
        return render(request, 'app_wealthway/templates/base.html', {'form': form, 'lp_metas': lp_metas})

def sucesso(request):
    return render(request, 'app_wealthway/templates/sucesso.html')