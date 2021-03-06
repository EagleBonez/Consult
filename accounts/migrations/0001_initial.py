# Generated by Django 2.2.9 on 2020-03-19 22:40

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
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(blank=True, max_length=100, null=True)),
                ('org_id', models.CharField(blank=True, max_length=5, null=True)),
                ('org_building_name_no', models.CharField(blank=True, max_length=100, null=True)),
                ('org_street', models.CharField(blank=True, max_length=100, null=True)),
                ('org_town', models.CharField(blank=True, max_length=100, null=True)),
                ('org_county', models.CharField(blank=True, max_length=100, null=True)),
                ('org_postcode', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['org_name'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_id', models.CharField(blank=True, max_length=5, null=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('house_name_no', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('county', models.CharField(blank=True, max_length=100, null=True)),
                ('postcode', models.CharField(blank=True, max_length=100, null=True)),
                ('tel', models.CharField(blank=True, max_length=100, null=True)),
                ('gdpr_consent', models.BooleanField(default=False)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Organisation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('client_last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('client_org', models.CharField(blank=True, max_length=100, null=True)),
                ('client_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
