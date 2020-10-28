# Generated by Django 3.1 on 2020-10-03 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_tel', models.CharField(max_length=30)),
                ('company_email', models.CharField(max_length=100)),
                ('channel', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=20, null=True)),
                ('camp_local', models.CharField(max_length=20, null=True)),
                ('camp_address', models.CharField(max_length=200, null=True)),
                ('camp_type', models.CharField(max_length=20, null=True)),
                ('content_offer', models.TextField()),
                ('content_keyword', models.TextField()),
                ('content_guide', models.TextField()),
                ('content_caution', models.TextField()),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('inserted_time', models.DateTimeField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('win_date', models.DateTimeField(blank=True, null=True)),
                ('img_path', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='campaign_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]