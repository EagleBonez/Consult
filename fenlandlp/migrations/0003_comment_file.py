# Generated by Django 2.2.9 on 2020-03-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fenlandlp', '0002_comment_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]