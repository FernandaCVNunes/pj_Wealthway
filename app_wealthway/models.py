from django.db import models
from django.core.exceptions import ValidationError

class Financas(models.Model):
    id_meta = models.AutoField(primary_key=True)
    nome_meta = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.CharField(max_length=300, blank=False, null=False)
    valor_total = models.FloatField(blank=False, null=False)
    valor_mensal = models.FloatField(blank=False, null=False)
    parcelas_totais = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'financas'
