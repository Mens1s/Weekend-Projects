# Generated by Django 3.2.9 on 2022-02-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='username',
            field=models.TextField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
