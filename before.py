from django.db import models


#===============================================================================
# This type of model inheritance works like normal inheritance. 
# In OOP when you inherit from another object you get all of its members plus your own. 
# You can modify those members or leave them the same. Abstract base classes are the same.
# There is also multi-table inheritance, proxy models, and multiple inheritance available.
#===============================================================================
 
 
 class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    purchase_history = models.ForeignKey('cart.Invoice')

class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    bio = models.TextField()
    position = models.CharField(max_length=20)