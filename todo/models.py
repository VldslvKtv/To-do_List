import datetime

from django.contrib.auth.models import User
from django.db import models
import datetime

EXECUTION_STATUS = [
    ('n', 'NOT_ACTIVE'),
    ('p', 'PROGRESS'),
    ('c', 'COMPLETED')
]


class Record(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField(null=True, editable=False)
    important = models.BooleanField(default=False)
    deadline = models.DateField(auto_now=False, null=True, blank=True)
    status = models.CharField(max_length=1, choices=EXECUTION_STATUS, default=EXECUTION_STATUS[1])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    objects = models.Manager()

    def __str__(self):  # отображение названий в админке
        return self.title
