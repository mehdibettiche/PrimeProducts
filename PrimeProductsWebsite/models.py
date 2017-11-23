from django.db import models


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=200, db_index=True)

    # keywords are stored as JSON object
    # make JSON-serialized (text) version of the keyword list
    # then store it in the DB. For example
    # >>> keywords_list = ['mountain', 'bike', 'sports']
    # >>> product.keywords = json.dumps(keywords_list)
    keywords = models.TextField(null=True)

    image = models.URLField(max_length=500, blank=True, default='')
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # this field is equivalent to status in the schema
    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    removed_at = models.DateTimeField(auto_now=True)

    # Q: Can many-to-one relation be encoded with a ForeignKey
    manufacturer = models.ForeignKey(Manufacturer)
    supermarket = models.ForeignKey(Supermarket)
    review = models.ForeignKey(Review)
    offer = models.ForeignKey(Offer)
    favorite = models.ForeignKey(Favorite)
    histroy = models.ForeignKey(History)


class Client(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    username = models.CharField(max_length=30, db_index=True, unique=True)
    password = models.CharField(max_length=30)
    contact = models.ForeignKey(ContactInfo)
    review = models.ForeignKey(Review)
    favorite = models.ForeignKey(favorite)
    histroy = models.ForeignKey(history)
    join_date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    stars = models.IntegerField(null=False, min_value=1, max_value=10)
    review_text = models.CharField(max_length=5000)
    review_date = models.DateTimeField(auto_now_add=True)

    # what exactly is the status here?
    status = models.BooleanField(default=True)

    # whats is reports number?
    num_reports = models.IntegerField(null=False, min_value=0)


class Supermarket(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    contact = models.ForeignKey(ContactInfo)
    opening_hours = models.CharField(max_length=50, db_index=True)
    review = models.ForeignKey(Review)


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    contact = models.ForeignKey(ContactInfo)
    review = models.ForeignKey(Review)


class ContactInfo(models.Model):
    location = models.CharField(max_length=50, db_index=True)
    country = models.CharField(max_length=50, db_index=True)
    phone_num = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(max_length=70,blank=True)

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    description = models.CharField(max_length=1000)

class Favorite(models.Model):
    client = models.ForeignKey(Client)
    product =  models.ForeignKey(Product)
