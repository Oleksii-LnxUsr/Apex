# Generated by Django 5.1.7 on 2025-03-19 22:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StakingStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField()),
                ('staking_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserStakingReward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StakingLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('min_deposite', models.IntegerField()),
                ('max_deposite', models.IntegerField()),
                ('percentage', models.IntegerField()),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staking.stakingstage')),
            ],
        ),
        migrations.CreateModel(
            name='UserStaking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('staking_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staking.stakinglevel')),
            ],
        ),
    ]
