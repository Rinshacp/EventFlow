# Generated by Django 5.1.3 on 2024-12-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_servicetable_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='date',
        ),
        migrations.AddField(
            model_name='feedback',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
