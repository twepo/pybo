# Generated by Django 3.1 on 2020-10-05 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lg', '0008_auto_20201005_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='created_time',
            new_name='inserted_time',
        ),
    ]
