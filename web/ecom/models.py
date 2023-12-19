from django.db import models

class items(models.Model):
    employee_id=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    city=models.CharField(max_length=20)
    dob=models.CharField(max_length=10)
    profession=models.CharField(max_length=20)
    salary=models.CharField(max_length=10)
    shift=models.CharField(max_length=20)
    age=models.CharField(max_length=10)
    
    class Meta:
        db_table="ecom"

class product(models.Model):
    order_id=models.CharField(max_length=20)
    employee_id=models.CharField(max_length=20)
    product=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    color=models.CharField(max_length=10)
    brand=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    model=models.CharField(max_length=20)
    date=models.CharField(max_length=10)

    class Meta:
        db_table="product"

class productcategory(models.Model):
    no=models.CharField(max_length=100)
    category=models.CharField(max_length=20)
    
    class Meta:
        db_table="category"

class categorizer(models.Model):
    product=models.CharField(max_length=25)
    category=models.CharField(max_length=25)

    class Meta:
        db_table="categorize_products"           


# Create your models here.
