# Generated by Django 2.1.5 on 2019-02-13 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0007_auto_20190212_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='user',
        ),
    ]
