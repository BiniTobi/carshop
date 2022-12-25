# Generated by Django 4.1.4 on 2022-12-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model', models.IntegerField()),
                ('transmition', models.CharField(max_length=150)),
                ('orignal_left_hand_or_not', models.CharField(max_length=150)),
                ('cc', models.CharField(max_length=150)),
                ('plate', models.CharField(max_length=150)),
                ('km', models.IntegerField()),
                ('condition', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
