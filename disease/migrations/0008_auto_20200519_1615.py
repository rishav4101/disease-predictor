# Generated by Django 3.0.6 on 2020-05-19 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0007_auto_20200519_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptoms',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
