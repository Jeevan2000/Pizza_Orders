"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demoapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.apiOverview,name="API Overview"),
    path('admin/', admin.site.urls),
    path('api/pizzalist/',views.pizzaList.as_view()),
    path('api/pizzatypes/',views.pizzaTypesList.as_view()),
    path('api/pizzadetail/<str:pk>/',views.pizzaDetail,name="Detail Information of Pizza"),
    path('api/createpizza/',views.createPizza,name="Create Pizza"),
    path('api/updatepizza/<str:pk>/',views.updatePizza,name="Update Pizza"),
    path('api/delpizza/<str:pk>/',views.deletePizza,name="Delete Pizza"),
    
]
