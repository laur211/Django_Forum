# Generated by Django 3.0.8 on 2020-07-27 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_forummodel_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ForumModel',
            new_name='TopicModel',
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('posted', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(blank=True, max_length=255)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.TopicModel')),
            ],
        ),
    ]