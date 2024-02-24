from django.db import models as m

from uuid import uuid4 as u4


class Funnel(m.Model):

    uid = m.UUIDField(default = u4)

    url = m.URLField()
    
    # user info

    ip = m.TextField(blank = True, null = True)
    country = m.TextField(blank = True, null = True)
    city = m.TextField(blank = True, null = True)


    mobile = m.BooleanField()

    # request time

    entered_at = m.DateTimeField()

    def __str__(self):

        return self.url