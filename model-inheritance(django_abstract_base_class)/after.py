from django.db import models


#===============================================================================
# As you can see these two models are legitimate models with fields, but they do have common elements. 
# In a lot of cases it is fine to leave them this way. 
# However, if we use these same fields yet again it would be a good idea to use an abstract base class.
# 
# We now have a ConactInfo abstract base class because we added abstract = True to its Meta. 
# This will tell django and the migration system this isn't a model we can use to store data with.
# 
# However, we can inherit from it so that each model that we subclass with it has the fields, methods, and properties of the abstract model. 
# At this point if you did ./manage.py makemigrations it would create a migration file creating only Customer and Staff tables in the database.
# My rule of thumb, whether good or bad, is if I have more than 3 fields repeated in only 2 models I just leave them alone. 
# If I need to add them to a third model I will evaluate if it makes sense to use an abstract model. 
# If I can name the abstract model and it makes sense like ContactInfo then there is enough context to create the new model, so I will. 
# Otherwise I will put it off until the code is screaming for an abstract base class.
# src: https://godjango.com/blog/django-abstract-base-class-model-inheritance/
#===============================================================================




class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Customer(ContactInfo):
    purchase_history = models.ForeignKey('cart.Invoice')

class Staff(ContactInfo):
    bio = models.TextField()
    position = models.CharField(max_length=20)