# Generated by Django 4.1.7 on 2023-02-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('time', models.IntegerField()),
            ],
        ),
    ]
