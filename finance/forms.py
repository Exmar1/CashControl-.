from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
		class Meta:
				model = Transaction
				fields = ["amount", 'transaction_type', 'category', 'date', 'description']
