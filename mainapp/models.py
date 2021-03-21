from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50, null=False)
    text = models.TextField(verbose_name='Новость')
    date = models.DateTimeField(verbose_name='Дата публикации', auto_now=True)

    class Meta:
        verbose_name = 'новостной пост'
        verbose_name_plural = 'новостные посты'

    def __str__(self):
        return self.title