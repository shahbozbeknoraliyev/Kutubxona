# Generated by Django 4.1.5 on 2023-01-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0006_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nashriyot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('manzil', models.CharField(max_length=100)),
            ],
        ),
    ]
