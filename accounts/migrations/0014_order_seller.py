# Generated by Django 3.1.3 on 2020-12-17 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_order_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='seller',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.seller'),
        ),
    ]