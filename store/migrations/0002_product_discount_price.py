# Generated by Django 3.2.5 on 2022-05-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]