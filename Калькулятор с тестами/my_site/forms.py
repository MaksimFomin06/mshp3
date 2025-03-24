from django import forms


class NumberForm(forms.Form):
    number_one = forms.IntegerField(label='Первое число', error_messages={'invalid': 'Введите правильное значение.'})
    number_two = forms.IntegerField(label='Второе число', error_messages={'invalid': 'Введите правильное значение.'})