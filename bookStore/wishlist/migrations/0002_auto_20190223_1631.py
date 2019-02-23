# Generated by Django 2.1.5 on 2019-02-23 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='list',
            name='user_name',
            field=models.CharField(max_length=150),
        ),
    ]
