# Generated by Django 3.2.9 on 2022-07-02 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ext_data', '0004_lidlproduct_lidlproductprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='abcproduct',
            name='avg_price_473_ml',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='abcproduct',
            name='best_price_473_ml',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
    ]
