# Generated by Django 3.0.5 on 2020-05-03 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200503_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]