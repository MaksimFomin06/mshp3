from django.test import TestCase, Client
from .models import CalculatorDB
from .forms import NumberForm

class FormTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_form_submission(self):
        response = self.client.post('/', {
            'number_one': 10,
            'number_two': 20,
        })
        
        self.assertEqual(response.status_code, 200)
        
        self.assertTrue(CalculatorDB.objects.filter(number_one=10, number_two=20).exists())
        
        self.assertContains(response, f'10 + 20 = 30')

    def test_invalid_input(self):
        response = self.client.post('/', {
            'number_one': 'abc',
            'number_two': 'def',
        })
        
        self.assertEqual(response.status_code, 200)
        
        self.assertFalse(CalculatorDB.objects.exists())

        content = response.content.decode('utf-8')
        self.assertIn('Введите правильное значение.', content)