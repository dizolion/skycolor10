# Generated by Django 4.0.3 on 2022-04-07 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, default='', max_length=200)),
                ('prof_name', models.CharField(blank=True, default='', max_length=200)),
                ('memo', models.CharField(blank=True, default='', max_length=200)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='subjectApp.subject')),
            ],
        ),
    ]
