from django.contrib import admin as a

from .models import *
from .task_models import *

@a.register(Photo)
class PhotoAdmin(a.ModelAdmin):

    list_display = ['email', 'image_size']

    def email(self, image):

        return image.uploader.username

    def image_size(self, image):

        size_in_MB = round(image.file.size / 1024 / 1024, 2)

        return f"{size_in_MB} MB"

@a.register(Note)
class NoteAdmin(a.ModelAdmin):

    list_display = ['author', 'created_at', 'updated_at']

a.site.register(Folder)

@a.register(UserPayment)
class UserPaymentAdmin(a.ModelAdmin):
    list_display = ('profile', 'paid_at', )

@a.register(Task)
class TaskAdmin(a.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']
