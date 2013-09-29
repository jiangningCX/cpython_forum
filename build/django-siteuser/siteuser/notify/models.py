# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


class Notify(models.Model):
    """
    link - 此通知链接到的页面
    text - 此通知的文字，也就是展示出来的内容
    """
    user = models.ForeignKey('users.SiteUser', related_name='notifies')
    sender = models.ForeignKey('users.SiteUser')
    link = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    notify_at = models.DateTimeField()
    has_read = models.BooleanField(default=False)

    def __unicode__(self):
        return u'<Notify %d>' % self.id

    @classmethod
    def create(cls, **kwargs):
        kwargs['notify_at'] = timezone.now()
        cls.objects.create(**kwargs)