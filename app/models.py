import os

from django.db import models as m

from django.contrib.auth.models import User

from user.models import Profile

from uuid import uuid4 as u4

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode


class Password(m.Model):
    
    uid = m.UUIDField(default = u4)
    
    user = m.ForeignKey(User, on_delete = m.CASCADE, related_name = 'users_password')
    
    title = m.TextField(blank = True, null = True)
    url = m.URLField(blank = True, null = True)
    username = m.TextField(blank = True, null = True)
    password = m.BinaryField(blank = True, null = True)
    note = m.TextField(blank = True, null = True)
    
    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)
    
    def __str__(self):
        
        return self.title
    
    class Meta:
        
        ordering = ['-updated_at']
        
    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)
        
    @staticmethod
    def encrypt_password(password, key):
        
        cipher = AES.new(key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(password.encode())
        return cipher.nonce + ciphertext