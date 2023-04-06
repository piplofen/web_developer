# Generated by Django 4.2 on 2023-04-06 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(db_index=True)),
                ('body', models.TextField(default='Комментарий')),
                ('date_published', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=150)),
                ('description', models.TextField(default='Описание книги')),
                ('photo', models.ImageField(upload_to='image')),
                ('date_published', models.CharField(max_length=10)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='book.comments')),
            ],
        ),
    ]
