from django.db import models
from django.db.models.deletion import CASCADE

CATEGORY_CHOICES = [('other', 'Разное'), ('toys', 'Игрушки'), ('for home', 'Для дома'), ('present', 'Подарки'),
                    ('in car', 'В машину'), ('hobby', 'Хобби'), ('for garden', 'Для сада')]


class Products(models.Model):
    product = models.CharField(max_length=100, verbose_name='Товар')
    description = models.TextField(max_length=2000, verbose_name='Описание')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name='Категории')
    remainder = models.PositiveIntegerField(verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость')

    def __str__(self):
        return f"{self.id}, {self.product}, {self.price}"

    class Meta:
        db_table = "Products"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Basket(models.Model):
    item = models.ForeignKey("Product.Products", on_delete=CASCADE, null=True, blank=True,
                             related_name="in_basket", verbose_name='Товар в корзине')
    count = models.PositiveIntegerField(verbose_name="Товара в корзине")

    def __str__(self):
        return f"{self.id}, {self.item}, {self.count}"

    class Meta:
        db_table = "Basket"
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"
