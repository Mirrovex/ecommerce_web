# Generated by Django 5.0.6 on 2024-05-24 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
