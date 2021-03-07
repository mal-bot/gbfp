from django.db import models


class Vacancy(models.Model):
    name = models.CharField(verbose_name='название', max_length=250, blank=True, null=True)
    description = models.CharField(verbose_name='описание', max_length=250, blank=True, null=True)

    # company = models.ForeignKey(Company, verbose_name='Компания', blank=True, null=True, on_delete=models.SET_NULL)

    draft = models.BooleanField(verbose_name='черновик', default=False)

    is_active = models.BooleanField(verbose_name='активен', default=False)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'

    def __str__(self):
        return self.name
