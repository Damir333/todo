# Generated by Django 3.1.3 on 2020-12-14 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_item', '0002_auto_20201214_1036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemmodel',
            old_name='listmodel_id',
            new_name='listmodel',
        ),
    ]
