# Generated by Django 3.0.8 on 2020-08-08 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_remove_topicmodel_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='content',
        ),
    ]
