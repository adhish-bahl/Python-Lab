# Generated by Django 3.0.14 on 2023-10-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('Name', models.CharField(max_length=30)),
                ('UserName', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=30)),
                ('Gender', models.CharField(max_length=6)),
            ],
        ),
    ]
