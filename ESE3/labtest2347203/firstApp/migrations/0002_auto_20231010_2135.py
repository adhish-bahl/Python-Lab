# Generated by Django 3.0.14 on 2023-10-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userId',
        ),
        migrations.AddField(
            model_name='user',
            name='PhoneNumber',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
