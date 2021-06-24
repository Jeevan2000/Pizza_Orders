# Pizza_Orders
Django RestFramework API

This is Django Pizza Orders App 
Here we made many different APIs to show ,add,delete data

In these app we have added users and different types of Pizza from Django Admin panel we have also validated users while adding Pizza Order.
In backend we have used MongoDB database

Different API's are as follows:

1. /api/pizzalist/ - this get request is used to return json data of all pizza orders having fiels(id,pizztype,pizzasize,pizzatopping,username)
2. /api/pizzatypes/ - this get request is used to return pizzatypes data only
3. /api/pizzadetail/<str:pk>/ - this is get request to get the detail of speific pizza order
4. /api/createpizza/- this post request is used to create pizza orders directly from API
5 /api/updatepizza/<str:pk>/ - this post request is used the update the data
6. /api/delpizza/<str:pk>/- this delete request is used to delete the data

All changes done in API are reflected in database(mongodb) and viceversa.
