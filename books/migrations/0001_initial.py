# Generated by Django 2.1.5 on 2019-04-14 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=10)),
                ('book_title', models.CharField(max_length=100)),
                ('book_genre', models.CharField(max_length=100)),
                ('book_plot', models.CharField(max_length=100)),
                ('book_link', models.CharField(max_length=100)),
                ('book_rating', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book_Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('book_id', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
