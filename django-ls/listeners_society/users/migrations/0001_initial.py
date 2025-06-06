# Generated by Django 5.2.1 on 2025-05-23 22:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=50)),
                ('admin_email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('role', models.CharField(choices=[('Volunteer Approver', 'Volunteer Approver'), ('User Support Manager', 'User Support Manager'), ('System Monitor', 'System Monitor')])),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('chat_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
                ('is_saved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('password', models.CharField(max_length=128)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('bio', models.CharField(blank=True, max_length=255)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('ChatMessage_id', models.AutoField(primary_key=True, serialize=False)),
                ('sender_id', models.PositiveIntegerField()),
                ('message_text', models.TextField(blank=True, max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('chat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.chat')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('volunteer_id', models.AutoField(primary_key=True, serialize=False)),
                ('volunteer_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=128)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')])),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('bio', models.CharField(blank=True, max_length=225)),
                ('expertise', models.CharField(max_length=50)),
                ('approved_date', models.DateTimeField(auto_now_add=True)),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.admin')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='volunteer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.volunteer'),
        ),
    ]
