# Generated by Django 4.1.4 on 2023-02-14 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Qpaper', '0009_alter_tourbooking_numberofrooms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourbooking',
            old_name='user',
            new_name='user_name',
        ),
    ]
