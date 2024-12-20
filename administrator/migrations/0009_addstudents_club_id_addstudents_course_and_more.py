# Generated by Django 5.1.3 on 2024-12-20 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0008_remove_notificationtable_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addstudents',
            name='CLUB_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.logintable'),
        ),
        migrations.AddField(
            model_name='addstudents',
            name='course',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='addstudents',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='addstudents',
            name='phoneno',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='addstudents',
            name='semester',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
