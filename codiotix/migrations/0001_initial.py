# Generated by Django 4.0.2 on 2022-02-18 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('actorImage', models.ImageField(upload_to='images/')),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Drama', 'Drama'), ('Action and Adventure', 'Action and Adventure'), ('Romance', 'Romance'), ('Comedy', 'Comedy'), ('Thriller', 'Thriller'), ('Horror', 'Horror')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_type', models.CharField(choices=[('Drama', 'Drama'), ('Action and Adventure', 'Action and Adventure'), ('Romance', 'Romance'), ('Comedy', 'Comedy'), ('Thriller', 'Thriller'), ('Horror', 'Horror')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Webserie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('desc', models.TextField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codiotix.genre')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codiotix.language')),
                ('tags', models.ManyToManyField(to='codiotix.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('video', models.FileField(upload_to='videos/')),
                ('desc', models.TextField()),
                ('cast', models.ManyToManyField(to='codiotix.Cast')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codiotix.genre')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codiotix.language')),
                ('tags', models.ManyToManyField(to='codiotix.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_number', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='videos/')),
                ('webserie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codiotix.webserie')),
            ],
        ),
    ]
