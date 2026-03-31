from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum

def index(request):
    expenses = Expense.objects.all()
    totals = Expense.objects.values('category').annotate(total=Sum('amount'))
    return render(request, 'expenses/index.html', {'expenses': expenses, 'totals': totals})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def delete_expense(request, id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect('index')