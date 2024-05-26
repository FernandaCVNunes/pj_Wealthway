from django.test import TestCase
from .models import Financas
from .forms import FinancasForm

class FinancasModelTest(TestCase):

    def setUp(self):
        self.financas1 = Financas.objects.create(
            nome_meta='Meta 1',
            descricao='Descrição 1',
            valor_total=1000,
            valor_mensal=100,
        )

    def test_nome_meta_unico(self):
        with self.assertRaises(Exception):
            Financas.objects.create(
                nome_meta='Meta 1',
                descricao='Descrição 2',
                valor_total=2000,
                valor_mensal=200,
            )

    def test_descricao_unico(self):
        with self.assertRaises(Exception):
            Financas.objects.create(
                nome_meta='Meta 2',
                descricao='Descrição 1',
                valor_total=2000,
                valor_mensal=200,
            )

class FinancasFormTest(TestCase):

    def test_form_valido(self):
        form_data = {
            'nome_meta': 'Meta 3',
            'descricao': 'Descrição 3',
            'valor_total': 3000,
            'valor_mensal': 300,
        }
        form = FinancasForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalido_nome_meta_duplicado(self):
        Financas.objects.create(
            nome_meta='Meta 4',
            descricao='Descrição 4',
            valor_total=4000,
            valor_mensal=400,
        )
        form_data = {
            'nome_meta': 'Meta 4',
            'descricao': 'Descrição 5',
            'valor_total': 5000,
            'valor_mensal': 500,
        }
        form = FinancasForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['nome_meta'], ['Nome da meta já existe.'])

    def test_form_invalido_descricao_duplicado(self):
        Financas.objects.create(
            nome_meta='Meta 6',
            descricao='Descrição 6',
            valor_total=6000,
            valor_mensal=600,
        )
        form_data = {
            'nome_meta': 'Meta 7',
            'descricao': 'Descrição 6',
            'valor_total': 7000,
            'valor_mensal': 700,
        }
        form = FinancasForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['descricao'], ['Descrição já existe.'])

    def test_form_invalido_valor_total_zero(self):
        form_data = {
            'nome_meta': 'Meta 8',
            'descricao': 'Descrição 8',
            'valor_total': 0,  # Valor total zero
            'valor_mensal': 100,
        }
        form = FinancasForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('valor_total', form.errors)
        self.assertEqual(form.errors['valor_total'], ['O valor total não pode ser zero.'])

    def test_form_invalido_valor_mensal_zero(self):
        form_data = {
            'nome_meta': 'Meta 9',
            'descricao': 'Descrição 9',
            'valor_total': 1000,
            'valor_mensal': 0,  # Valor mensal zero
        }
        form = FinancasForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('valor_mensal', form.errors)
        self.assertEqual(form.errors['valor_mensal'], ['O valor mensal não pode ser zero.'])

    def test_form_invalido_campos_obrigatorios(self):
        form_data = {
            'nome_meta': '',
            'descricao': '',
            'valor_total': '',
            'valor_mensal': '',
        }
        form = FinancasForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['nome_meta'], ['Este campo é obrigatório.'])
        self.assertEqual(form.errors['descricao'], ['Este campo é obrigatório.'])
        self.assertEqual(form.errors['valor_total'], ['Este campo é obrigatório.'])
        self.assertEqual(form.errors['valor_mensal'], ['Este campo é obrigatório.'])