# Generated by Django 4.1.6 on 2023-02-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('year', models.IntegerField(max_length=50)),
                ('Description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField(max_length=50)),
                ('Employee_number', models.IntegerField(max_length=50)),
                ('Description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('Department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField(max_length=50)),
                ('Employee_number', models.IntegerField(max_length=50)),
                ('Description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('Department', models.CharField(max_length=50)),
            ],
        ),
    ]
