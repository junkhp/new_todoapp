from django.db import models
from django.utils import timezone

# Create your models here.

PRIORITY = (('danger', '高い'), ('warning', '普通'), ('primary', '低い'))


class ToDoModel(models.Model):

    class Meta(object):
        db_table = 'todo'

    STATUS_CHOICES = [
        ('doing', '未完了'),
        ('done', '完了'),
    ]
    title = models.CharField(max_length=200, verbose_name='タイトル')
    memo = models.TextField(verbose_name='詳細', blank=True, null=True, default='詳細なし')
    priority = models.CharField(max_length=50, choices=PRIORITY,
                                verbose_name='優先度', default='warning')
    duedate = models.DateField(verbose_name='締め切り日', default=timezone.now)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,
                              verbose_name='状況', default='doing')

    def __str__(self):
        return self.title


class HowtoOrder(models.Model):
    class Meta(object):
        db_table = 'how_to_order'
    ORDERS = [
        ('creation_order', '作成された順'), ('due_order', '締め切り順'), ('priority_order', '優先度順')
    ]
    REVERSE = [
        ('ascending', '昇順'), ('descending', '降順')
    ]
    order = models.CharField(max_length=50, verbose_name='並び順',
                             choices=ORDERS, default='creation_order')
    ascending_or_descending = models.CharField(max_length=50, verbose_name='昇順か降順か',
                                               choices=REVERSE, default='descending')

    def __str__(self):
        return self.order
