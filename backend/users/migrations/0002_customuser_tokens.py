# Generated by Django 5.1.7 on 2025-03-19 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='tokens',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
