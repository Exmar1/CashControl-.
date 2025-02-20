from django import forms
from .models import Transaction

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


