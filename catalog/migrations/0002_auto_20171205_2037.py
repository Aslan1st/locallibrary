# Generated by Django 2.0 on 2017-12-06 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='book', max_length=200),
        ),
    ]
