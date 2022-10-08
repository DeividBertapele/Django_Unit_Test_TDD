from django.test import TestCase
from ..models import Pessoa


class PessoaTestCase(TestCase):
    
    def setUp(self):
        Pessoa.objects.create(
            nome='Dj',
            idade=39
        )
    
    def test_returno_str(self):
        p1 = Pessoa.objects.get(nome='Dj')
        self.assertEquals(p1.__str__(), 'Dj')