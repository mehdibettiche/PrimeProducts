from django.contrib import admin

# Register your models here.
#To make our model visible on the admin page, we need to register all model

from	.models	import Category
from	.models	import ContactInfo
from	.models	import History
from	.models	import Client
from	.models	import Review
from	.models	import Supermarket
from	.models	import Manufacturer
from	.models	import Product
from	.models	import Favorite

admin.site.register(Category)
admin.site.register(ContactInfo)
admin.site.register(History)
admin.site.register(Client)
admin.site.register(Review)
admin.site.register(Supermarket)
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(Favorite)
