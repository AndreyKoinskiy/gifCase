from django.contrib import admin

from .models import Mp4UploaderModel, GifUploaderModel
# Register your models here.
@admin.register(Mp4UploaderModel)
class Mp4UploaderModelAdmin(admin.ModelAdmin):
    pass

@admin.register(GifUploaderModel)
class GifUploaderModelAdmin(admin.ModelAdmin):
    pass
