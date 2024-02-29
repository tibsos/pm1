import os

from django.db import models as m

from django.contrib.auth.models import User

from user.models import Profile

from uuid import uuid4 as u4

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


def upload_photo(instance, filename):

    file_extenstion = filename.split('.')[-1]
    new_filename = f"{u4}.{file_extenstion}"

    return os.path.join('uploads/note/images', new_filename)

class UserPayment(m.Model):

    uid = m.UUIDField(default = u4)
    
    premium = m.BooleanField(default = False)
    profile = m.ForeignKey(Profile, on_delete = m.DO_NOTHING)

    paid_at = m.DateTimeField(auto_now_add = True)

    def __str__(self):

        return self.profile.user.username

class Photo(m.Model):

    uid = m.UUIDField(default = u4)

    uploader = m.ForeignKey(User, on_delete = m.CASCADE)

    note = m.ForeignKey('Note', on_delete = m.CASCADE)

    file = m.ImageField(upload_to = upload_photo)

    uploaded_at = m.DateTimeField(auto_now_add = True)

    def __str__(self):

        return self.uploader.username

    def save(self, *args, **kwargs):
        # Open the image
        img = Image.open(self.file)

        if img.mode == 'RGBA':
            img = img.convert('RGB')

        # Resize and compress the image
        output = BytesIO()
        img = img.resize((300, 300))  # Resize the image as needed
        img.save(output, format='JPEG', quality=10)  # Adjust quality as needed

        output.seek(0)
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.file.name.split('.')[0],
                                          'image/jpeg', sys.getsizeof(output), None)

        super(Photo, self).save(*args, **kwargs)

class Note(m.Model):

    uid = m.UUIDField(default = u4) # unique id

    author = m.ForeignKey(User, on_delete = m.CASCADE)
    #co_authors = m.ManyToManyField(User, blank = True, related_name = 'note_coauthors') # author != co-author

    folders = m.ManyToManyField('Folder', blank = True, related_name = 'note_folders')

    title = m.TextField()
    content = m.TextField()

    photos = m.ManyToManyField(Photo, blank = True, related_name = 'note_photos')

    loved = m.BooleanField(default = False)
    pinned = m.BooleanField(default = False)
    archived = m.BooleanField(default = False)

    deleted = m.BooleanField(default = False)
    deleted_at = m.DateTimeField(auto_now = True)

    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        return self.author.username

    class Meta:

        ordering = ['-updated_at']

class Folder(m.Model):

    uid = m.UUIDField(default = u4)

    author = m.ForeignKey(User, on_delete = m.CASCADE)

    title = m.CharField(max_length = 50)

    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        return self.title

    class Meta:

        ordering = ['-updated_at']