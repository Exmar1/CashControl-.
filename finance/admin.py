from django.contrib import admin
from .models import CustomUser, Category, Transaction, Goal, Budget

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Goal)
admin.site.register(Budget)

