from django.db import models as m

from django.contrib.auth.models import User

from uuid import uuid4 as u4

class Task(m.Model):

    uid = m.UUIDField(default = u4)
    user = m.ForeignKey(User, on_delete = m.CASCADE)

    title = m.TextField()

    completed = m.BooleanField(default = False)
    priority = m.PositiveSmallIntegerField(default = 1)

    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        return f"{UserWithTasks(self.user)} | {self.user.username}"


class UserWithTasks(User):

    class Meta:

        proxy = True

    def total_tasks(self):

        return Task.objects.filter(user=self).count()