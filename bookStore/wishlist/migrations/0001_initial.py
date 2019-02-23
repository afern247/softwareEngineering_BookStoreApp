# Generated by Django 2.1.5 on 2019-02-23 21:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0010_auto_20190216_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author_name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_name', models.CharField(default='Testing', max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='list_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wishlist.List'),
        ),
    ]
