from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Stock, Purchase


@receiver(post_save, sender=Purchase)
def update_stock(sender, instance, **kwargs):
    stock = Stock.objects.get(available_item=instance.item)
    print(f"Mavjud mahsulotlar miqdori: --- {stock.available_quantity}")
    stock.available_quantity = stock.available_quantity - instance.quantity
    stock.save()
    print(f"Sotilgan mahsulot miqdori: --- {instance.quantity}\n"
          f"Qolgan mahsulot miqdori: --- {stock.available_quantity} ")
