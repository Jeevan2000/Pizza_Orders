from django import db
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.relations import ManyRelatedField
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
#from rest_framework.filters import SearchFilter,OrderingFilter
from .models import *
from .serializer import *

# Create your views here.
class pizzaList(APIView):

    def get(self,request):
        piz=PizzaTypes.objects.all()
        serializers=PizzaTypesSerializer(piz, many=True)
        return Response(serializers.data)
        
    #print([e.username for e in Customer.objects.all()])
class pizzaTypesList(APIView):

    def get(self,request):
        piz=PizzaTypes.objects.all()
        serializers=PizzaTypes1Serializer(piz, many=True)
        return Response(serializers.data)   

@api_view(['GET'])
def apiOverview(request):
    apiurls={
        'PizzaList':'/pizzaList/',
        'PizzaTypesList':'/pizzaTypesList/',
        'DetailPizza':'/pizzadetails/<str:pk>/',
        'CreatePizza':'api/createpizza/',
        'UpdatePizza':'api/updatepizza/<str:pk>/',
        'DeletePizza':'api/delpizza/<str:pk>/'
    }     
    return Response(apiurls)

# get method to get single pizza detail
@api_view(['GET'])
def pizzaDetail(request,pk):
    piz=PizzaTypes.objects.get(id=pk)
    serializers=PizzaTypesSerializer(piz, many=False)
    return Response(serializers.data)  

# create method 
@api_view(['POST'])
def createPizza(request):
    serializers=PizzaTypesSerializer(data=request.data)
    # name=(serializers.initial_data.get('username'))
    # res=[e.username for e in Customer.objects.all()] 
    serializers.validate(data=request.data)  
    if not serializers.is_valid():
        return Response({'status':403,'errors':serializers.errors,'message':'Something went wrong'})
    
    return Response(serializers.data)

#update method
@api_view(['POST'])
def updatePizza(request,pk):
    piz=PizzaTypes.objects.get(id=pk)
    serializers=PizzaTypesSerializer(instance=piz,data=request.data)
    serializers.validate(data=request.data)
    if serializers.is_valid():
        serializers.save()
    else:
        serializers.default_error_messages    
    
    return Response(serializers.data)                       

#delete method 
@api_view(['DELETE'])
def deletePizza(request,pk):
    piz=PizzaTypes.objects.get(id=pk)
    piz.delete()
    return Response("Item deleted Successfully !!")

# filter by search
'''
class UserListView(generics.ListAPIView):
    queryset = PizzaTypes.objects.all()
    serializer_class = PizzaTypesSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['pizza_toppings','pizza_sizes','pizza_types']   
   
'''