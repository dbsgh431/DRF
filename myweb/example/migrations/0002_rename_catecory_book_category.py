# Generated by Django 4.0.6 on 2022-08-31 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='catecory',
            new_name='category',
        ),
    ]
