# Generated by Django 3.1 on 2020-11-01 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201101_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valueofsplitedata',
            name='splitusername',
        ),
        migrations.AddField(
            model_name='adddevice',
            name='devicerybdata',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.valueofsplitedata'),
        ),
    ]
