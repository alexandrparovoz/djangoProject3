from django.db import models

class Task(models.Model):
    name = models.CharField(name='task_name', max_length=255)
    text = models.CharField(name='text', max_length=255)
    time = models.IntegerField(name='time')

    def __str__(self):
        return self.text