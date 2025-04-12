from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    photo_of_product = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def clean(self):
        if self.price < 0:
            raise ValidationError({
                'price': 'Цена не может быть отрицательной. '
            })
        if self.quantity_in_stock < 0:
            raise ValidationError({
                'quantity_in_stock': 'Остаток не может быть отрицательным. '
            })


class Cart(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Корзина пользователя: {self.user.username}"

    def total_cost(self):
        return sum(item.item_cost() for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} ({self.quantity} шт)"

    def item_cost(self):
        return self.product.price * self.quantity

    def clean(self):
        if self.quantity > self.product.quantity_in_stock:
            raise ValidationError('Количество товара в корзине не может превышать количество товара на складе.'
                                  )
