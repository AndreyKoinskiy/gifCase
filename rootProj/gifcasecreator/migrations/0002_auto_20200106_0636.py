# Generated by Django 2.2 on 2020-01-06 04:36

from django.db import migrations, models
import utilities


class Migration(migrations.Migration):

    dependencies = [
        ('gifcasecreator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mp4UploaderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('file_mp4', models.FileField(upload_to=utilities.get_upload_path)),
                ('slug', models.SlugField(blank=True, max_length=120)),
            ],
        ),
        migrations.RenameModel(
            old_name='CaseMp4ToGifUploader',
            new_name='GifUploaderModel',
        ),
        migrations.RenameField(
            model_name='gifuploadermodel',
            old_name='file',
            new_name='file_gif',
        ),
    ]
