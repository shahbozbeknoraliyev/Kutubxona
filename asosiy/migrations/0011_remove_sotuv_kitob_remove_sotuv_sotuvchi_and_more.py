# Generated by Django 4.1.5 on 2023-01-11 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0010_alter_sotuvchi_tel_sotuv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sotuv',
            name='kitob',
        ),
        migrations.RemoveField(
            model_name='sotuv',
            name='sotuvchi',
        ),
        migrations.DeleteModel(
            name='Kitob1',
        ),
        migrations.DeleteModel(
            name='Nashriyot',
        ),
        migrations.DeleteModel(
            name='Sotuv',
        ),
        migrations.DeleteModel(
            name='Sotuvchi',
        ),
    ]
