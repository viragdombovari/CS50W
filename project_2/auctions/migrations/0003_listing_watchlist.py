# Generated by Django 5.1.4 on 2024-12-13 11:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_category_id_alter_listing_id_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchList',
            field=models.ManyToManyField(blank=True, null=True, related_name='listingWatchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
