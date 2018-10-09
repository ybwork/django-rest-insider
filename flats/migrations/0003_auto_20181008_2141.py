# Generated by Django 2.1 on 2018-10-08 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flats', '0002_flat_house'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.House'),
        ),
    ]
