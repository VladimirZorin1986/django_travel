from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    country = models.CharField(max_length=100, verbose_name='Страна')

    def __str__(self):
        return f'{self.name}({self.country})'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']
