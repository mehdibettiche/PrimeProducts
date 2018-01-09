from django.db import models

## Les classe (base de données) de PrimeProducts
class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    description = models.CharField(max_length=1000)


class ContactInfo(models.Model):
    location = models.CharField(max_length=50, db_index=True)
    country = models.CharField(max_length=50, db_index=True)
    phone_num = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(max_length=70,blank=True)

class History(models.Model):
    query = models.CharField(max_length=500)


class Client(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    username = models.CharField(max_length=30, db_index=True, unique=True)
    password = models.CharField(max_length=30)
    contact = models.ForeignKey(
    'ContactInfo',
    on_delete=models.CASCADE,
    )
    histroy = models.ForeignKey(
    'History',blank=True,null=True,
    on_delete=models.CASCADE,
    )
    join_date = models.DateTimeField(auto_now_add=True)

class Supermarket(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    contact = models.ForeignKey(
    'ContactInfo',
    on_delete=models.CASCADE,
    )
    opening_hours = models.CharField(max_length=50, db_index=True)
    review = models.ForeignKey(
    'Review',blank=True,null=True,
    on_delete=models.CASCADE,
    )

class Manufacturer(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    contact = models.ForeignKey(
    'ContactInfo',
    on_delete=models.CASCADE,
    )
    review = models.ForeignKey(
    'Review',blank=True,null=True,
    on_delete=models.CASCADE,
    )

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,)
    name = models.CharField(max_length=200, db_index=True)
    keywords = models.TextField(null=True)

    image = models.CharField(max_length=200,null=True,blank=True, default='')
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    removed_at = models.DateTimeField(auto_now=True)

    manufacturer = models.ForeignKey(
    'Manufacturer',
    on_delete=models.CASCADE,
    )
    supermarket = models.ForeignKey(
    'Supermarket',
    on_delete=models.CASCADE,
    )
    review = models.ForeignKey(
    'Review',blank=True,null=True,
    on_delete=models.CASCADE,
    )
    histroy = models.ForeignKey(
    'History',blank=True,null=True,
    on_delete=models.CASCADE,
    )

class Favorite(models.Model):
    product =  models.ForeignKey(
    'Product',blank=True,null=True,
    on_delete=models.CASCADE,
    )


class Review(models.Model):
    username = models.CharField(max_length=50, db_index=True)
    stars = models.DecimalField(null=False, max_digits=1, decimal_places=0)
    review_text = models.CharField(max_length=5000)
    review_date = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=500)
