# Generated by Django 5.0.6 on 2024-05-19 06:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('work_price', models.IntegerField()),
                ('work_time', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('count_sold', models.IntegerField()),
                ('birthday', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id', 'firstname', 'lastname'],
                'indexes': [models.Index(fields=['id', 'firstname', 'lastname', 'username'], name='users_agent_id_dc86ba_idx')],
            },
        ),
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=30)),
                ('problem_name', models.CharField(max_length=30)),
                ('problem_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id', 'created_at'],
                'indexes': [models.Index(fields=['id', 'username'], name='users_probl_id_9fb641_idx')],
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_title', models.CharField(max_length=200)),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id', 'user'],
                'indexes': [models.Index(fields=['id', 'user'], name='users_comme_id_75ef4e_idx')],
            },
        ),
    ]