from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Category(models.Model):
	name = models.CharField(max_length=100)
	user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Transaction(models.Model):
	TRANSACTION_TYPE = (
		('income', 'Доход'),
		('expense', 'Расход'),
	)

	CATEGORY_CHOICES = (
		('cars', 'Автомобиль'),
		('food', 'Продукты'),
		('rent', 'Аренда'),
		('salary', 'Зарплата'),
		('entertainment', 'Развлечения'),

)

	user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	transaction_type = models.CharField(max_length=9, choices=TRANSACTION_TYPE)
	category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
	date = models.DateTimeField(null=True, blank=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return f"{self.transaction_type} - {self.amount} {self.date}"
	

class Budget(models.Model):
	user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
	category = models.CharField(max_length=20, choices=Transaction.CATEGORY_CHOICES)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	date = models.DateField()

	def __str__(self):
		return f"Бюджет на {self.category} - {self.amount}"
	
class Goal(models.Model):
	user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	target_amount = models.DecimalField(max_digits=10, decimal_places=2)
	current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	deadline = models.DateField(null=True, blank=True)
	

	def __str__(self):
		return f"Цель: {self.name} - {self.target_amount}"
