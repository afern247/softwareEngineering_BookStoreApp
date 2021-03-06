# Generated by Django 2.1.5 on 2019-04-05 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookDetails', '0003_auto_20190324_2010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='text',
            new_name='message',
        ),
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=3),
        ),
    ]
