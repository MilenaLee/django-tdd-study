# Generated by Django 2.2.3 on 2019-07-14 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_auto_20190715_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='lists',
            new_name='list',
        ),
    ]