# Generated by Django 2.2 on 2020-01-05 23:03

from django.db import migrations, models
import utilities


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseMp4ToGifUploader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('file', models.FileField(upload_to=utilities.get_upload_path)),
                ('slug', models.SlugField(blank=True, max_length=120)),
            ],
        ),
    ]
