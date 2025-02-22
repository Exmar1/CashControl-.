from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from finance.models import CustomUser as User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TransactionForm, BudgetForm
from django.contrib import messages
from .models import Transaction, Budget
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def home(request):
     if request.method == 'POST' and 'save_budget' in request.POST:
         budget = Budget.objects.filter(user=request.user).first()
         budget_form = BudgetForm(request.POST, instance=budget)
         if budget_form.is_valid():
             new_budget = budget_form.save(commit=False)
             new_budget.user = request.user
             new_budget.save()
             return redirect('home')
     else:
         form = TransactionForm()
         budget = Budget.objects.filter(user=request.user).first()
         budget_form = BudgetForm(instance=budget)

     transactions = Transaction.objects.filter(user=request.user).order_by('-date')

     return render(request, 'finance/home.html', {
        "form": form,
        "budget_form": budget_form,
        "transaction": transactions,
        "budget": budget
    })



def signup_user(request):
    if request.method == 'GET':
        return render(request, 'finance/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save() 
                login(request, user)
                return redirect('current_finance')
            except: IntegrityError
            return render(request, 'finance/signupuser.html', {'form':UserCreationForm(), 'error':'Имя пользователя уже существует, пожалуйста задайте новое'})
        else:
            return render(request, 'finance/signupuser.html', {'form':UserCreationForm(), 'error':'Пароли не совпадают'})

def login_user(request):
    if request.method == 'GET':
        return render(request, 'finance/signupuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'finance/signupuser.html', {'form':AuthenticationForm(), 'error':' Username And Password Did not match'})
        else:
           login(request, user)
           return redirect('current_finance')

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def completed_finance(request):
    transactions = Transaction.objects.filter(user=request.user, date__isnull=False).order_by('-date')
    return render(request, 'finance/transactions_list.html', {'transactions': transactions})

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, 'Транзакция успешно сохранена')
            return redirect('home') 
        else:
            messages.error(request, 'Ошибка при сохранении транзакции. Проверьте введенные данные.')
            form = BudgetForm()

        return render(request, 'finance/home.html', {'form':form})
    
@login_required
def delete_transaction(request, finance_pk):
    transaction = get_object_or_404(Transaction, id=finance_pk, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('completed_finance')


@login_required
def add_budget(request):
    form = TransactionForm()
    budgets = Budget.objects.filter(user=request.user).order_by('-date')
    if request.method == 'POST':
        if "save_transaction" in request.POST:
            form = TransactionForm(request.POST)
            if form.is_valid():
                transaction = form.save(commit=False)
                transaction.user = request.user
                transaction.save()
                return redirect("home")
            
        elif "save_budget" in request.POST:
            budget_form = BudgetForm(request.POST, instance=budgets)
            if budget_form.is_valid():
                new_budget = budget_form.save(commit=False)
                new_budget.user = request.user
                new_budget.save()
                return redirect('home')
            
    return render(request, 'finance/home.html', {
        "form":form,
        "budget_form":budget_form,
        "transaction": transaction,
        "budgets":budgets
    })


      

                    