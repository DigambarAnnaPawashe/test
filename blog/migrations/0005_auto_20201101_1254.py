# Generated by Django 3.1 on 2020-11-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201101_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valueofsplitedata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
