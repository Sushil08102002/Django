# Generated by Django 3.2.24 on 2024-08-26 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20240826_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=16),
        ),
    ]
