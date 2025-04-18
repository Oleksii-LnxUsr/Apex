# Generated by Django 5.1.7 on 2025-04-06 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staking', '0009_stakingstage_days_for_change'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Wallets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('wallet', models.CharField(max_length=48)),
            ],
        ),
    ]
