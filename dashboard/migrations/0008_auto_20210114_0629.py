# Generated by Django 3.1.4 on 2021-01-14 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20210114_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='click_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]