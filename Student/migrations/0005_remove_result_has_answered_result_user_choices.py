# Generated by Django 4.0.6 on 2024-10-06 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0004_alter_result_has_answered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='has_answered',
        ),
        migrations.AddField(
            model_name='result',
            name='user_choices',
            field=models.JSONField(default={''}),
        ),
    ]