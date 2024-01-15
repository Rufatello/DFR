from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(max_length=150, verbose_name='Почта', unique=True)
    surname = models.CharField(max_length=150, verbose_name='Отчество', blank=True, null=True)
    phone = models.ImageField(max_length=15, verbose_name='Телефон', blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name='Город', blank=True, null=True)
    avatar = models.ImageField(upload_to='user/', verbose_name='Аватар', blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='course/', verbose_name='Фото')
    descriptions = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title} {self.descriptions}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    descriptions = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='course/', verbose_name='Фото', blank=True, null=True)
    link_video = models.CharField(max_length=150, verbose_name='Название', blank=True, null=True)

    def __str__(self):
        return f'{self.title} {self.descriptions}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
