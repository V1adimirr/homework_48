# Generated by Django 4.0.6 on 2022-07-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100, verbose_name='Товар')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('category', models.CharField(choices=[('other', 'Разное'), ('toys', 'Игрушки'), ('for home', 'Для дома'), ('present', 'Подарки'), ('in car', 'В машину'), ('hobby', 'Хобби'), ('for garden', 'Для сада')], default='other', max_length=30, verbose_name='Категории')),
                ('remainder', models.PositiveIntegerField(verbose_name='Остаток')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'Products',
            },
        ),
    ]
