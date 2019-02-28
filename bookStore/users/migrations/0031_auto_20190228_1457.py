# Generated by Django 2.1.5 on 2019-02-28 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20190228_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Profile'),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='addresses',
        ),
        migrations.AddField(
            model_name='profile',
            name='addresses',
            field=models.ManyToManyField(to='users.Address'),
        ),
    ]