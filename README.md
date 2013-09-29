本站点使用v2ex风格,代码参考 feather;

1. 安装依赖
 'grappelli' 后台管理风格
  python manage.py collectstatic

 'django-message'后台信息管理
  安装方法：python easy_install django-messages
  
  'django-pagination'文章分页
  安装方法：python easy_install django-pagination

2.有关于simple报错处理

将django-messages下urls.py中的from django.views.generic.simple import redirect_to
修改为：

from django.views.generic import RedirectView

urlpatterns = patterns('',
    (r'^one/$', RedirectView.as_view(url='/another/')),
)
