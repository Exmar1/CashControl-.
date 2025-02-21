from django import forms
from .models import Transaction, Budget

class TransactionForm(forms.ModelForm):
		date = forms.DateTimeField(
			widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
			required=False
		)

		amount = forms.DecimalField(
			widget=forms.NumberInput(attrs={'step': '0.01'})
		)

		class Meta:
				model = Transaction
				fields = ['amount', 'transaction_type', 'category', 'date', 'description']

class BudgetForm(forms.ModelForm):
	date = forms.DateTimeField(
			widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
			required=False
		)
	
	amount = forms.DecimalField(
			widget=forms.NumberInput(attrs={'step': '0.01'})
		)

	class Meta:
		model = Budget
		fields = ['amount', 'date']


