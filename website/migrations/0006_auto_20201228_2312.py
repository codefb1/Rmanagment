# Generated by Django 3.1.4 on 2020-12-28 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20201228_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='numtab',
            field=models.IntegerField(max_length=255, null=True),
        ),
    ]
