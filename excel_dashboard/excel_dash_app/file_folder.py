import csv 
from .models import product , order , brand , Seller

def file_data(filepath):

    with open(filepath, mode="r") as f:
        filed = csv.DictReader(f)

        for r in filed:

            brand_obj, _ = brand.objects.get_or_create(
                brand_name=r['brand']
            )

            Seller_obj, _ = Seller.objects.get_or_create(
                seller_name=r['seller'],
                seller_rating=r['seller_rating'],
                seller_city=r['seller_city']
            )

            product_obj, _ = product.objects.get_or_create(
                product_id=r['product_id'],
                product_name=r['product_name'],
                product_units_sold=r['units_sold'],
                product_warranty=r['warranty_months'],
                product_return_days=r['return_policy_days'],
                product_is_returnable=r['is_returnable'],
                product_score=r['product_score'],
                product_rating=r['rating'],
                product_stock_available=r['stock_available'],
                product_brand=brand_obj,
                product_seller=Seller_obj,
                product_color=r['color'],
                product_discount=r['discount_percent']
            )

            order_obj, _ = order.objects.get_or_create(
                order_product=product_obj,
                order_delivery_date=r['delivery_days'],
                order_final_price=r['final_price'],
                order_payemnt_method=r['payment_modes']
            )