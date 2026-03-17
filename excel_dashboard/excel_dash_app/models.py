from django.db import models

# Create your models here.
class brand(models.Model):
    brand_name = models.TextField(choices=[('Adidas', 'Adidas'), ('Apple', 'Apple'), ('Boat', 'Boat'), ('Dell', 'Dell'), ('HP', 'HP'), ('IG', 'IG'), ('Nike', 'Nike'), ('Philips', 'Philips'), ('Prestige', 'Prestige'), ('Puma', 'Puma'), ('Redmi', 'Redmi'), ('Reebok', 'Reebok'), ('Samsung', 'Samsung'), ('Sony', 'Sony'), ('Whirlpool', 'Whirlpool')], max_length=100)

    def __str__(self):
        return self.brand_name
class Seller(models.Model):
    seller_name = models.TextField(max_length=100)
    seller_rating = models.FloatField()
    seller_city = models.TextField(max_length=100)
    
    def __str__(self):
        return self.seller_name

class product(models.Model):
    product_id = models.CharField(unique=True , primary_key=True)
    product_name = models.TextField(max_length=100)
    product_units_sold = models.IntegerField()
    product_warranty = models.IntegerField()
    product_return_days = models.IntegerField()
    product_is_returnable = models.BooleanField()
    product_score = models.FloatField()
    product_rating = models.FloatField()
    product_stock_available = models.IntegerField()

    product_brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    product_seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_color = models.TextField(max_length=100)
    product_discount = models.FloatField()
    
    def __str__(self):
        return self.product_name
    

    
class order(models.Model):
    order_product = models.ForeignKey(product, on_delete=models.CASCADE)
    order_delivery_date = models.IntegerField()
    order_final_price = models.FloatField()
    order_payemnt_method = models.TextField(choices= [(("CARD,Wallet"), "CARD,Wallet"), (("COD,CARD"), "COD,CARD"), (("COD,UPI,CARD"), "COD,UPI,CARD"), (("UPI,CARD"), "UPI,CARD")], max_length=100)
    def __str__(self):
        return f"{self.order_product.product_name} - {self.order_delivery_date}"
    
class filemodel(models.Model):
    file = models.FileField(upload_to='files/')