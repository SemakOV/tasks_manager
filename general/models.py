from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)# null=True)
    title = models.CharField('Название', max_length=45)
    description = models.TextField('Описание')
    time_create = models.DateTimeField('Время создания', auto_now_add=True)
    state = models.CharField('Статус', max_length=40)
    time_out = models.DateField('Дата завершения')

    # def get_absolut_url(self):

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


# Create your models here.
