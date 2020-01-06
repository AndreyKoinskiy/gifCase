import os
from django.db import models
from django.core.files import File
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from utilities import get_upload_path, to_gif


# Create your models here.

class GifUploaderModel(models.Model):
    title = models.CharField(max_length=120)
    file_gif = models.FileField(upload_to=get_upload_path)
    slug = models.SlugField(max_length=120, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        return super(GifUploaderModel, self).save(*args, **kwargs)


class Mp4UploaderModel(models.Model):
    title = models.CharField(max_length=120)
    file_mp4 = models.FileField(upload_to=get_upload_path)
    slug = models.SlugField(max_length=120, blank=True)

    def __str__(self):
        return self.title

    @receiver(post_save, sender=User)
    def save(self, *args, **kwargs):
        is_extension_valid = self.file_mp4.name[-4:].lower() == '.mp4'
        print("Extension: ", self.file_mp4.name[-4:].lower())
        to_save = kwargs.get('to_save', True)

        if is_extension_valid:
            size_of_file = self.file_mp4.size / 1024 / 1024
            path = get_upload_path(self, self.file_mp4.name)
            full_path = os.path.join(settings.BASE_DIR, "media", path)
            print("Full_path: ", full_path)
            print("Size: ", size_of_file)
            if size_of_file >= 2.5:
                super(Mp4UploaderModel, self).save(*args, **kwargs)

                to_gif(full_path)
                gif_path = full_path[:-4]+'.gif'

                gif_obj = GifUploaderModel.objects.create()
                with open(gif_path, 'rb') as converted_gif:
                    gif = File(converted_gif)
                    # file_gif.save(gif_name, gif)
                    gif_obj.file_gif.save(gif.name,gif)
                gif_obj.title = self.title
                gif_obj.slug = self.slug
                gif_obj.save()
                self.delete()
                print(self)
        else:
            default_path = os.path.join(settings.BASE_DIR, "media", "default\\default.mp4")
            with open(default_path, 'rb') as default_mp4:
                mp4 = File(default_mp4) 
                self.file_mp4.save(mp4.name, mp4)
        return super(Mp4UploaderModel, self).save(*args, **kwargs)

def delete_large_mp4(sender, instance, **kwargs):
    print(type(instance))
    if (instance.file_mp4.size / 1024 / 1024) > 2.5:
        print("Вызиваю Удаление")
        instance.delete()

post_save.connect(delete_large_mp4,sender=Mp4UploaderModel)