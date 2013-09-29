# -*- coding: utf-8 -*-

import json

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured
from django.template import RequestContext

from siteuser.notify.models import Notify
from siteuser.utils import load_user_define

"""
这只是一个简单的通知系统，产生的通知格式如下：
［谁］在［哪个条目/帖子］中回复了你
因为在生成的通知里有 ［谁］ 这个用户链接，所以用户必须自己在settings.py中定义 USER_LINK
这个方法，它接受一个参数：用户id，然后返回用户个人页面的url

有两种方式获取通知：
    1. GET /notifies.json/ 返回的是未读的通知，只要用js将返回的html组织在合适dom元素中即可
    2. GET /notifies/      用一个页面来展示全部的通知。包括已经处理过的通知

所以就必须设置 SITEUSER_ACCOUNT_MIXIN, 在其中指定 notify_template

点击一个未读的通知:
    GET /notify/confirm/<notify_id>/ 如果正确，就会跳转到相应的页面
"""


user_define = load_user_define.user_defined_mixin()()
notify_template = getattr(user_define, 'notify_template', None)
if not notify_template:
    raise ImproperlyConfigured('SITEUSER_ACCOUNT_MIXIN has no attribute "notify_template"')

get_notify_context = getattr(user_define, 'get_notify_context', None)
if not get_notify_context:
    get_notify_context = lambda x: {}

def notifies_json(request):
    """由Ajax获取的未读通知"""
    user = request.siteuser
    if not user:
        return HttpResponse(json.dumps([]), mimetype='application/json')

    notifies = Notify.objects.filter(user=user, has_read=False).select_related('sender').order_by('-notify_at')
    def _make_html(n):
        return u'<a href="{0}" target="_blank">{1}</a> 在 <a href="{2}" target="_blank">{3}</a> 中回复了你'.format(
            settings.USER_LINK(n.sender.id),
            n.sender.username,
            reverse('siteuser_notify_confirm', kwargs={'notify_id': n.id}),
            n.text,
        )
    html = [_make_html(n) for n in notifies]
    return HttpResponse(json.dumps(html), mimetype='application/json')


def get_notifies(request):
    """页面展示全部通知"""
    user = request.siteuser
    if not user:
        return HttpResponseRedirect(reverse('siteuser_login'))

    notifies = Notify.objects.filter(user=user).select_related('sender').order_by('-notify_at')
    # TODO 分页
    ctx = get_notify_context(request)
    ctx['notifies'] = notifies
    return render_to_response(
        notify_template,
        ctx,
        context_instance=RequestContext(request)
    )


def notify_confirm(request, notify_id):
    """点击通知上的链接，将此通知设置为has_read=True，然后转至此通知的link"""
    try:
        n = Notify.objects.get(id=notify_id)
    except Notify.DoesNotExist:
        raise Http404

    if not n.has_read:
        n.has_read = True
        n.save()

    return HttpResponseRedirect(n.link)