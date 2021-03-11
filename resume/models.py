from django.db import models
from authapp.models import User


class Resume(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        # name должно быть видно только соискателю
        name = models.CharField(verbose_name='название', max_length=250, blank=True, null=True)
        cellphone = models.BigIntegerField(verbose_name='номер телефона')
        comment = models.CharField(verbose_name='описание', max_length=250, blank=True, null=True)
        hide_comment = models.BooleanField(verbose_name='Комментарий к резюме виден только Вам', default=True)
        is_draft = models.BooleanField(verbose_name='черновик', default=False)
        created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
        updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)
        is_active = models.BooleanField(verbose_name='активен', default=False)
        job_list = models.TextField(verbose_name='опыт работы', blank=True, default='')
        salary = models.FloatField(verbose_name='Ожидаемая заработная плата', blank=True, default=0)
        key_words = models.TextField(verbose_name='ключевы навыки', blank=True, default='')
        education = models.TextField(verbose_name='образование', blank=True, default='')
        languages = models.TextField(verbose_name='знание языков', blank=True, default='')

        def _calc_experience(self):
            '''
            Calculates years and months of experience
            '''
            pass

        total_exp = property(_calc_experience)

        @property
        def _get_user_email(self):
            return self.user.email

        email = _get_user_email

        class Meta:
            ordering = ('name',)
            verbose_name = 'резюме'
            verbose_name_plural = 'резюме'

        def __str__(self):
            return f'{self.name} ({self.comment})'
