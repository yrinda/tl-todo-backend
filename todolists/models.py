from django.db import models
import uuid

# Create your models here.


class Todolist(models.Model):
    id = models.UUIDField(auto=True, primary_key=True,
                          default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
