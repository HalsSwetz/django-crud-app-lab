# Generated by Django 5.2 on 2025-04-03 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_critic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='critic',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2),
        ),
    ]
