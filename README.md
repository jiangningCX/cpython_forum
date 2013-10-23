本站点使用v2ex风格,代码参考 feather;

1. 安装依赖
 'grappelli' 后台管理风格
  python manage.py collectstatic

 'django-message'后台信息管理
  安装方法：python easy_install django-messages
  
  'django-pagination'文章分页
  安装方法：python easy_install django-pagination
  
  'DjangoUeditor'富文本编辑器
  安装方法：pip install DjangoUeditor
  
  
2.有关于simple报错处理

将django-messages下urls.py中的from django.views.generic.simple import redirect_to
修改为：

from django.views.generic import RedirectView

urlpatterns = patterns('',
    (r'^one/$', RedirectView.as_view(url='/another/')),
)

3.DjangoUeditor中富文本框的size调整，在editor_config.js中“,initialFrameWidth:500  //初始化编辑器宽度,默认1000”
对后面的数值进行修改，对应自己的网页可以做适当调整。

