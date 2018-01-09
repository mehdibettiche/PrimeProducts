# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, db_index=True)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, db_index=True)),
                ('username', models.CharField(max_length=30, unique=True, db_index=True)),
                ('password', models.CharField(max_length=30)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('location', models.CharField(max_length=50, db_index=True)),
                ('country', models.CharField(max_length=50, db_index=True)),
                ('phone_num', models.CharField(max_length=50, db_index=True)),
                ('email', models.EmailField(max_length=70, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('query', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, db_index=True)),
                ('contact', models.ForeignKey(to='PrimeProductsWebsite.ContactInfo', on_delete=models.CASCADE,)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('keywords', models.TextField(null=True)),
                ('image', models.URLField(max_length=500, blank=True, default='')),
                ('description', models.CharField(max_length=1000)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('removed_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(related_name='products', to='PrimeProductsWebsite.Category', on_delete=models.CASCADE,)),
                ('histroy', models.ForeignKey(to='PrimeProductsWebsite.History', on_delete=models.CASCADE,)),
                ('manufacturer', models.ForeignKey(to='PrimeProductsWebsite.Manufacturer', on_delete=models.CASCADE,)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('stars', models.DecimalField(max_digits=1, decimal_places=0)),
                ('review_text', models.CharField(max_length=5000)),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('author', models.ForeignKey(to='PrimeProductsWebsite.Client', on_delete=models.CASCADE,)),
            ],
        ),
        migrations.CreateModel(
            name='Supermarket',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, db_index=True)),
                ('opening_hours', models.CharField(max_length=50, db_index=True)),
                ('contact', models.ForeignKey(to='PrimeProductsWebsite.ContactInfo', on_delete=models.CASCADE,)),
                ('review', models.ForeignKey(to='PrimeProductsWebsite.Review', on_delete=models.CASCADE,)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='review',
            field=models.ForeignKey(to='PrimeProductsWebsite.Review', on_delete=models.CASCADE,),
        ),
        migrations.AddField(
            model_name='product',
            name='supermarket',
            field=models.ForeignKey(to='PrimeProductsWebsite.Supermarket', on_delete=models.CASCADE,),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='review',
            field=models.ForeignKey(to='PrimeProductsWebsite.Review', on_delete=models.CASCADE,),
        ),
        migrations.AddField(
            model_name='favorite',
            name='product',
            field=models.ForeignKey(to='PrimeProductsWebsite.Product', on_delete=models.CASCADE,),
        ),
        migrations.AddField(
            model_name='client',
            name='contact',
            field=models.ForeignKey(to='PrimeProductsWebsite.ContactInfo', on_delete=models.CASCADE,),
        ),
        migrations.AddField(
            model_name='client',
            name='histroy',
            field=models.ForeignKey(to='PrimeProductsWebsite.History', on_delete=models.CASCADE,),
        ),
    ]
