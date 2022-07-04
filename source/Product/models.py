from django.db import models

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
