# Generated by Django 3.1 on 2020-10-15 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lg', '0014_campaign_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='channel',
            new_name='channel_title',
        ),
    ]
