from django.contrib import admin
from .models import GroceryList, GroceryItem
# Register your models here.
admin.site.register(GroceryList)
admin.site.register(GroceryItem)