# Generated by Django 2.1.1 on 2020-02-10 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='hot',
            new_name='type',
        ),
    ]