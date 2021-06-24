from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField

# Create your models here.
class Customer(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username

class PizzaTypes(models.Model):
    
    #u1=Customer.objects.get('username')
    username=models.ForeignKey(Customer,on_delete=CASCADE)
    type_of_pizza=[('regular','Regular'),
                   ('square','Square')]
    pizza_types=models.CharField(max_length=12,choices=type_of_pizza,default='regular')

    type_of_sizes=[('extra small','Extra Small'),
    ('small','Small'),
    ('medium','Medium'),
    ('medium large','Medium Large'),
    ('large','Large'),
    ('extra large','Extra Large')]
    pizza_sizes=models.CharField(max_length=15,choices=type_of_sizes,default='medium')

    type_of_toppings=[('onion','Onion'),
    ('tomato','Tomato'),
    ('corn','Corn'),
    ('cheese','Cheese'),
    ('capsicum','Capsicum'),
    ('jalapeno','Jalapeno')]
    pizza_toppings=models.CharField(max_length=12,choices=type_of_toppings,default='cheese')

    def __str__(self):
        return self.pizza_toppings


            