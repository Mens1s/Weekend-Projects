# Generated by Django 4.0.2 on 2022-02-06 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_rename_inversting balance_myuser_btcbalance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='firstname',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='lastname',
            field=models.CharField(max_length=150),
        ),
    ]