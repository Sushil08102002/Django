# Generated by Django 5.1 on 2024-08-29 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=20)),
                ('genere', models.CharField(max_length=30)),
            ],
        ),
    ]
