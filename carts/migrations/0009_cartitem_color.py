# Generated by Django 4.2.4 on 2023-09-14 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_product_user_alter_product_users_wishlist'),
        ('carts', '0008_alter_cart_coupon_delete_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.color'),
        ),
    ]
