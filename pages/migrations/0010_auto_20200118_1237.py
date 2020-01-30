# Generated by Django 3.0.1 on 2020-01-18 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0009_auto_20200118_1216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='timestam',
            new_name='date_comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='content',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='massage',
            field=models.TextField(default=1, verbose_name='Message'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.Detail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]