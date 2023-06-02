# Generated by Django 4.2.1 on 2023-05-30 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.CharField(max_length=150)),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register_user.qualification')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=15)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('resume', models.FileField(upload_to='resumes/')),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('highest_qualification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='register_user.qualification')),
                ('specialized_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='register_user.subject')),
            ],
        ),
    ]
