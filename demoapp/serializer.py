from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import *

class PizzaTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model=PizzaTypes
        fields='__all__'
       

    def validate(self, data):
        res=[e.username for e in Customer.objects.all()]
        if data['username'] not in res:
            raise serializers.ValidationError({'status':403,'error':'Username not registered'})
        return data    

class PizzaTypes1Serializer(serializers.ModelSerializer):

    class Meta:
        model=PizzaTypes
        fields=['id','pizza_types']        