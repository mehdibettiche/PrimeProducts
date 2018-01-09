
The implemented functions in views.py are :

  1- def categories_listing : to list all category in DB and the number of products in each one
  
  
  2- def search_query : to show the searching text 'entered by the user' in result page 
  
  
  3- def result_page: show the resulting product corresponding to search query (without giving the cheapest product and not take care of all possible cases of search query)
  
  
  4-def product_details :give information about product (without review ,I'll work on it ..)
  
 
The keywords for searching until now are :

legumes pot bœuf

lait bebe

COUCHES BABY TAILLE 3

pizza 4 fromages

#To access into admin page and modify DB :

http://127.0.0.1:8000/admin/

userName :admin

passWord:admin

#Notice :I've used django 2.1

For every modivication in model.py we have to alter Django about it by :


1-to let Django know that we have some changes in our model.

 python3 manage.py makemigrations PrimeProductsWebsite

2-Django	prepared a migration file for us that we now have to apply to our database.

$ python3 manage.py migrate PrimeProductsWebsite

#To get into Django' interactive console and try some QuerySet :
$ python3 manage.py shell

>>> from PrimeProductsWebsite.models import Product

>>> Product.objects.all()

<QuerySet [<Product: Product object (1)>, <Product: Product object (2)>, <Product: Product object (3)>]>

#get one product from Product table

>>> Product.objects.filter(price='12.71')

<QuerySet [<Product: Product object (1)>]>

 Work to be done :
 
 1- Script for take care of all possible cases of searching query
 
 2- singup/singIn 
 
 3- show user profile photo depending on the first letter in user's name
