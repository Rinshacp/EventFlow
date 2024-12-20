# Generated by Django 5.1.3 on 2024-12-20 09:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0009_addstudents_club_id_addstudents_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addstudents',
            name='STUDENT_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studentid', to='administrator.logintable'),
        ),
        migrations.AlterField(
            model_name='addstudents',
            name='CLUB_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clubid', to='administrator.logintable'),
        ),
    ]