# Generated by Django 3.2.5 on 2024-03-09 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diabetesapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('mail', models.CharField(max_length=30)),
                ('message', models.TextField(max_length=300)),
            ],
        ),
    ]
