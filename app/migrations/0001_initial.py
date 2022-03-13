# Generated by Django 4.0.3 on 2022-03-13 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('organization', models.CharField(max_length=20)),
                ('orgId', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(default='Default Competetion', max_length=20)),
                ('competitionId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('difficulty', models.CharField(blank=True, default='Easy', max_length=20)),
                ('isPublic', models.BooleanField(default=True, max_length=20)),
                ('startTime', models.CharField(default='1647169487000', editable=False, max_length=20)),
                ('update_at', models.CharField(default='1647169487000', editable=False, max_length=20)),
                ('duration', models.PositiveIntegerField(default=1800)),
                ('description', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('questionType', models.CharField(max_length=50)),
                ('options', models.CharField(max_length=50)),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.interview')),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(default='+91 xxxxxxxxxx', max_length=20)),
                ('badge', models.PositiveIntegerField(default=1)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interviewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(default='+91 xxxxxxxxxx', max_length=20)),
                ('experience', models.PositiveIntegerField(default=2)),
                ('examiner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='interview',
            name='interviewer',
            field=models.ManyToManyField(related_name='interviewer', to='app.interviewer'),
        ),
        migrations.AddField(
            model_name='interview',
            name='participants',
            field=models.ManyToManyField(to='app.participants'),
        ),
    ]