from django.shortcuts import render
from .forms import NumberForm
from .models import CalculatorDB


def index_page(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            number_one = form.cleaned_data['number_one']
            number_two = form.cleaned_data['number_two']
            
            number_ans = number_one + number_two
            CalculatorDB.objects.create(number_one=number_one, number_two=number_two, number_ans=number_ans)
            
            context = {'data': CalculatorDB.objects.all()}
            return render(request, 'my_site/index.html', context)
    
    else:
        form = NumberForm()
    
    return render(request, 'my_site/index.html', {'form': form})