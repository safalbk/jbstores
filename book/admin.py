from django.contrib import admin
from .models import Persons, Transactions

# Register your models here.
admin.site.register(Persons)

admin.site.register(Transactions)
