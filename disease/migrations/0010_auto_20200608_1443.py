# Generated by Django 3.0.7 on 2020-06-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0009_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]