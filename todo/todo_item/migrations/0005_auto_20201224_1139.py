# Generated by Django 3.1.3 on 2020-12-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_item', '0004_auto_20201224_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listitem',
            name='expare_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
