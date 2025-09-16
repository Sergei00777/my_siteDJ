from django.db import models

from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    profession = models.CharField(max_length=100, verbose_name='Профессия')
    about = models.TextField(verbose_name='О себе')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    photo = models.ImageField(upload_to='photos/', null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

class Experience(models.Model):
    position = models.CharField(max_length=100, verbose_name='Должность')
    company = models.CharField(max_length=100, verbose_name='Компания')
    period = models.CharField(max_length=50, verbose_name='Период')
    description = models.TextField(verbose_name='Описание')

class Education(models.Model):
    institution = models.CharField(max_length=100, verbose_name='Учебное заведение')
    specialty = models.CharField(max_length=100, verbose_name='Специальность')
    period = models.CharField(max_length=50, verbose_name='Период')

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name='Навык')
    level = models.IntegerField(verbose_name='Уровень (0-100)')

class PortfolioItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    # Временно убираем изображение
    # image = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    link = models.URLField(blank=True, verbose_name='Ссылка')

class Diploma(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    institution = models.CharField(max_length=100, verbose_name='Учреждение')
    year = models.IntegerField(verbose_name='Год')
    # Временно убираем файл
    # file = models.FileField(upload_to='diplomas/', null=True, blank=True)