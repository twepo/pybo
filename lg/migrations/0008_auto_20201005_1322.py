# Generated by Django 3.1 on 2020-10-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lg', '0007_auto_20201004_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='inserted_time',
        ),
        migrations.AddField(
            model_name='campaign',
            name='created_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
