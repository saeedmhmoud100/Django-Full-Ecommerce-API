# Generated by Django 4.2.4 on 2023-09-04 17:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0009_alter_product_users_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='users_wishlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='wishList', to=settings.AUTH_USER_MODEL),
        ),
    ]
