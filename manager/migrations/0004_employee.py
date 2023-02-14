# Generated by Django 4.1.6 on 2023-02-12 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField(max_length=50)),
                ('Employee_number', models.IntegerField(max_length=50)),
                ('Description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.department')),
                ('Department_head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.departmenthead')),
            ],
        ),
    ]
