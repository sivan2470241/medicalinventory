# Generated by Django 4.2.1 on 2023-06-05 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='specializations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=20)),
                ('photo', models.ImageField(max_length=200, upload_to='photos/')),
                ('resume', models.FileField(max_length=500, upload_to='resumes/')),
                ('highest_qualification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.qualification')),
                ('specialized_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.specializations')),
            ],
        ),
    ]
