from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class GroceryList(models.Model):
    # users = models.ForeignKey(Profile, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='grocery_list')
    name = models.CharField()

    def __str__(self):
        return self.name



class GroceryItem(models.Model):
    food = models.CharField()
    list = models.ForeignKey(GroceryList, related_name="items",on_delete=models.CASCADE)

    def __str__(self):
        return self.food


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    

# Create your models here.
