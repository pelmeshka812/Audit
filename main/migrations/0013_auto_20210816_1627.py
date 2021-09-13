# Generated by Django 3.2.4 on 2021-08-16 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_measure_subprocess_measures'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measure',
            old_name='level',
            new_name='levels',
        ),
        migrations.RenameField(
            model_name='sentence',
            old_name='sentence',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='sentence',
            name='measure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentences', to='main.measure'),
        ),
    ]
