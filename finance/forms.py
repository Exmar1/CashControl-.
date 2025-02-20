from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
		class Meta:
				model = Transaction
<<<<<<< HEAD
				fields = ['amount', 'transaction_type', 'category', 'date', 'description']
=======
				fields = ["amount", 'transaction_type', 'category', 'date', 'description']
>>>>>>> 8c4f7ee48b96989f4f15c8815fe6f6ed98bdccd1
