# Generated by Django 3.0.6 on 2020-06-30 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forummodel',
            name='content',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
