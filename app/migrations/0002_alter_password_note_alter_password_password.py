# Generated by Django 5.0.1 on 2024-04-30 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='password',
            name='password',
            field=models.BinaryField(blank=True),
        ),
    ]
