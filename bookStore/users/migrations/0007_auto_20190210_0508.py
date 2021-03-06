# Generated by Django 2.1.5 on 2019-02-10 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190210_0439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(default='Miami', max_length=60)),
                ('state', models.CharField(default='Florida', max_length=30)),
                ('zipcode', models.CharField(default='33165', max_length=5)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.PositiveIntegerField(choices=[(1, 'Home address'), (2, 'Shipping address')])),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Address')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='addresses',
            field=models.ManyToManyField(through='users.AddressInfo', to='users.Address'),
        ),
    ]
