# Generated by Django 3.2.4 on 2021-07-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210713_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measure',
            name='level',
        ),
        migrations.AddField(
            model_name='measure',
            name='level',
            field=models.ManyToManyField(to='main.ProtectionLevel'),
        ),
    ]
