# Generated by Django 3.1.4 on 2021-01-14 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_click'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='click_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
