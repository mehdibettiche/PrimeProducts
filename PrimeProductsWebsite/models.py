from django.db import models


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
    #favorite = models.ForeignKey(Favorite)
    histroy = models.ForeignKey(
    'History',
    on_delete=models.CASCADE,
    )
    join_date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    stars = models.DecimalField(null=False, max_digits=1, decimal_places=0)
    review_text = models.CharField(max_length=5000)
    review_date = models.DateTimeField(auto_now_add=True)

    # what exactly is the status here?
    status = models.BooleanField(default=True)
    author = models.ForeignKey(
    'Client',
    on_delete=models.CASCADE,
    )
    # whats is reports number?
    #num_reports = models.IntegerField(null=False, min_value=0)

class Supermarket(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    contact = models.ForeignKey(
    'ContactInfo',
    on_delete=models.CASCADE,
    )
    opening_hours = models.CharField(max_length=50, db_index=True)
    review = models.ForeignKey(
    'Review',
    on_delete=models.CASCADE,
    )

class Manufacturer(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    contact = models.ForeignKey(
    'ContactInfo',
    on_delete=models.CASCADE,
    )
    review = models.ForeignKey(
    'Review',
    on_delete=models.CASCADE,
    )

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,)
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

    # Q: Can many-to-one relation be encoded with a ForeignKey?
    manufacturer = models.ForeignKey(
    'Manufacturer',
    on_delete=models.CASCADE,
    )
    supermarket = models.ForeignKey(
    'Supermarket',
    on_delete=models.CASCADE,
    )
    review = models.ForeignKey(
    'Review',
    on_delete=models.CASCADE,
    )
    #offer = models.ForeignKey(Offer)
    #favorite = models.ForeignKey(Favorite)
    histroy = models.ForeignKey(
    'History',
    on_delete=models.CASCADE,
    )

class Favorite(models.Model):
    #client = models.ForeignKey(Client)
    product =  models.ForeignKey(
    'Product',
    on_delete=models.CASCADE,
    )
