# Generated by Django 5.0.6 on 2024-05-19 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id', 'name'],
                'indexes': [models.Index(fields=['id'], name='projectapp__id_704177_idx')],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id', 'name'],
                'indexes': [models.Index(fields=['id'], name='projectapp__id_2f44c8_idx')],
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.city')),
            ],
            options={
                'ordering': ['id', 'name'],
            },
        ),
        migrations.CreateModel(
            name='SellType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id', 'name'],
                'indexes': [models.Index(fields=['id', 'name'], name='projectapp__id_0b9e11_idx')],
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('square', models.IntegerField()),
                ('seller_phone', models.CharField(max_length=20)),
                ('seller_name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('rooms', models.IntegerField()),
                ('count_bath', models.IntegerField()),
                ('count_floor', models.IntegerField()),
                ('count_bedrooms', models.IntegerField()),
                ('build_date', models.DateField(auto_now=True)),
                ('reconstruct_date', models.DateField(auto_now=True)),
                ('views', models.IntegerField()),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='media/apartment/photos/')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='media/apartment/photos/')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='media/apartment/photos/')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='media/apartment/photos/')),
                ('photo5', models.ImageField(blank=True, null=True, upload_to='media/apartment/photos/')),
                ('photo6', models.ImageField(blank=True, null=True, upload_to='media/apartment/photos/')),
                ('photo7', models.ImageField(blank=True, null=True, upload_to='media/apartment/photos/')),
                ('photo8', models.ImageField(blank=True, null=True, upload_to='media/apartment/photos/')),
                ('photo9', models.ImageField(blank=True, null=True, upload_to='media/apartment/photos/')),
                ('photo10', models.ImageField(blank=True, null=True, upload_to='media/apartment/photos/')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.address')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.category')),
                ('sell_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.selltype')),
            ],
            options={
                'ordering': ['id', 'short_name'],
            },
        ),
        migrations.AddIndex(
            model_name='address',
            index=models.Index(fields=['id', 'name'], name='projectapp__id_99e048_idx'),
        ),
        migrations.AddIndex(
            model_name='apartment',
            index=models.Index(fields=['id', 'short_name', 'photo1'], name='projectapp__id_13575a_idx'),
        ),
    ]
