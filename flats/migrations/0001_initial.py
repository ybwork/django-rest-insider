# Generated by Django 2.1 on 2018-10-08 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=10)),
                ('number', models.PositiveIntegerField(db_index=True)),
                ('entrance', models.PositiveIntegerField(db_index=True)),
                ('floor', models.PositiveIntegerField(db_index=True)),
                ('status', models.IntegerField(db_index=True)),
                ('clone_for_flats', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('type', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]