# Generated by Django 5.0.2 on 2024-02-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_products_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
