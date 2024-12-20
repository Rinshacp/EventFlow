# Generated by Django 5.1.3 on 2024-12-03 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clubtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('place', models.CharField(blank=True, max_length=30, null=True)),
                ('post', models.CharField(blank=True, max_length=30, null=True)),
                ('pin', models.IntegerField(blank=True, null=True)),
                ('phoneno', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='instructions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructions', models.CharField(blank=True, max_length=60, null=True)),
                ('date', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoginTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('password', models.CharField(blank=True, max_length=30, null=True)),
                ('usertype', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(blank=True, max_length=60, null=True)),
                ('date', models.CharField(blank=True, max_length=20, null=True)),
                ('time', models.CharField(blank=True, max_length=60, null=True)),
                ('reply', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ratingclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(blank=True, max_length=60, null=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=30, null=True)),
                ('rules', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(blank=True, max_length=30, null=True)),
                ('level', models.CharField(blank=True, max_length=30, null=True)),
                ('CLUB', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.clubtable')),
            ],
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(blank=True, max_length=60, null=True)),
                ('date', models.CharField(blank=True, max_length=60, null=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('CLUB', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.clubtable')),
            ],
        ),
        migrations.CreateModel(
            name='collegetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('place', models.CharField(blank=True, max_length=30, null=True)),
                ('post', models.CharField(blank=True, max_length=30, null=True)),
                ('pin', models.IntegerField(blank=True, null=True)),
                ('phoneno', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('LOGIN_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.logintable')),
            ],
        ),
        migrations.AddField(
            model_name='clubtable',
            name='LOGIN_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.logintable'),
        ),
        migrations.CreateModel(
            name='schooltable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('place', models.CharField(blank=True, max_length=30, null=True)),
                ('post', models.CharField(blank=True, max_length=30, null=True)),
                ('pin', models.IntegerField(blank=True, null=True)),
                ('phoneno', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('LOGIN_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.logintable')),
            ],
        ),
        migrations.CreateModel(
            name='servicetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services', models.CharField(blank=True, max_length=60, null=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('CLUB', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.clubtable')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('gender', models.CharField(blank=True, max_length=30, null=True)),
                ('phoneno', models.IntegerField(blank=True, null=True)),
                ('DOB', models.CharField(blank=True, max_length=30, null=True)),
                ('place', models.CharField(blank=True, max_length=30, null=True)),
                ('post', models.CharField(blank=True, max_length=30, null=True)),
                ('pin', models.IntegerField(blank=True, null=True)),
                ('LOGIN_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.logintable')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(blank=True, max_length=60, null=True)),
                ('date', models.CharField(blank=True, max_length=60, null=True)),
                ('USER', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.user')),
            ],
        ),
        migrations.CreateModel(
            name='complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaints', models.CharField(blank=True, max_length=60, null=True)),
                ('date', models.CharField(blank=True, max_length=60, null=True)),
                ('reply', models.CharField(blank=True, max_length=60, null=True)),
                ('USER', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.user')),
            ],
        ),
    ]
