import datetime
from django.conf import settings
from django.db import models

class TodoItem(models.Model):
    STATUS_CHOICES = [
        ('To-do', 'To-do'),
        ('Do today', 'Do today'),
        ('In Process', 'In Process'),
        ('Done', 'Done'),
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateField(default=datetime.date.today)
    due_date = models.DateField(default=datetime.date.today)
    priority = models.PositiveSmallIntegerField(default="3")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Todo')

    def __str__(self): 
        return f'({self.id}) {self.title}'