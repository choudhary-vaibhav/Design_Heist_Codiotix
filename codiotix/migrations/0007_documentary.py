# Generated by Django 4.0.2 on 2022-02-26 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codiotix', '0006_genre_image_language_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='movieimg/')),
                ('video', models.FileField(upload_to='movies/')),
                ('desc', models.TextField()),
                ('cast', models.ManyToManyField(to='codiotix.Cast')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codiotix.genre')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codiotix.language')),
                ('tags', models.ManyToManyField(to='codiotix.Tag')),
            ],
        ),
    ]
