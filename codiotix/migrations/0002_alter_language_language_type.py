# Generated by Django 4.0.2 on 2022-02-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codiotix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='language_type',
            field=models.CharField(choices=[('Hindi', 'Hindi'), ('English', 'English'), ('Tamil', 'Tamil'), ('Telegu', 'Telegu'), ('Malayalam', 'Malayalam'), ('Kannada', 'Kannada'), ('Marathi', 'Marathi'), ('Bengali', 'Bengali'), ('Punjabi', 'Punjabi'), ('Gujarati', 'Gujarati')], max_length=50),
        ),
    ]
