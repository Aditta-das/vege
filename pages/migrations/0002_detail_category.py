# Generated by Django 3.0.1 on 2019-12-25 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='category',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]