# Generated by Django 2.2 on 2020-05-30 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_product_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='battery',
        ),
        migrations.AddField(
            model_name='product',
            name='os',
            field=models.CharField(default='', max_length=20),
        ),
    ]
