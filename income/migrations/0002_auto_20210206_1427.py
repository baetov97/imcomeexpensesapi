# Generated by Django 3.1.6 on 2021-02-06 14:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expense',
            new_name='Income',
        ),
    ]
