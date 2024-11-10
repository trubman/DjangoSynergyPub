from django.db import models
from django.urls import reverse_lazy


class Human(models.Model):
    first_name = models.CharField(max_length=150, verbose_name = 'Имя')
    middle_name = models.CharField(max_length=150, verbose_name = 'Отчество (Прозвище)')
    last_name = models.CharField(max_length=150, verbose_name = 'Фамилия')
    biography = models.TextField(blank=True, verbose_name = 'Биография')
    date_of_birth = models.DateTimeField(verbose_name = 'Дата рождения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Дата изменения')
    passport_photo = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name = 'Фото на паспорт')
    is_adult = models.BooleanField(default=True, verbose_name = 'Совершеннолетие')
    profession = models.ForeignKey('Profession',
                                   on_delete=models.PROTECT,
                                   null=True,
                                   verbose_name='Профессия')

    def get_absolute_url(self):
        # return reverse_lazy('human_view', kwargs={'human_id': self.pk})
        return reverse_lazy('human_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Человеки'
        ordering = ['-created_at']


class Profession(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Профессия')

    def get_absolute_url(self):
        return reverse_lazy('profession', kwargs={'profession_id': self.pk})

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        ordering = ['title']

