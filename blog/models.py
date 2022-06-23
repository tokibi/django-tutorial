from django.db import models

# Create your models here.
class Article (models.Model):
    title = models.CharField('タイトル', max_length=255, unique=True)
    body = models.TextField('本文')
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.title
