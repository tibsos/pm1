from django.db import models as m

from tinymce.models import HTMLField

from django.urls import reverse

class Post(m.Model):

    title = m.TextField()
    description = m.TextField()
    content = HTMLField()

    slug = m.SlugField(max_length = 60, unique = True)

    thumbnail = m.ImageField(upload_to = 'blog/posts/thumbnails')

    views = m.PositiveSmallIntegerField()

    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        return self.title
    
    class Meta:

        ordering = ['-updated_at']

    def get_absolute_url(self):

        return reverse('blog:post', kwargs={'slug': self.slug})