# Generated by Django 3.2.12 on 2022-04-02 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('profile_picture', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=5)),
                ('review', models.TextField(blank=True, max_length=2000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=200)),
                ('release_year', models.CharField(blank=True, max_length=25)),
                ('director', models.CharField(max_length=100)),
                ('writer', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, max_length=900)),
                ('picture', models.ImageField(blank=True, upload_to='upload/')),
                ('actors', models.ManyToManyField(to='ProjectIMDB.Actor')),
                ('genre', models.ManyToManyField(to='ProjectIMDB.Genre')),
                ('rating', models.ManyToManyField(to='ProjectIMDB.Rating')),
            ],
        ),
    ]
