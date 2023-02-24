# Generated by Django 4.1.7 on 2023-02-24 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('call_back_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('problem', models.CharField(default='', max_length=250)),
                ('solution', models.CharField(default='', max_length=250)),
                ('incident_number', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]