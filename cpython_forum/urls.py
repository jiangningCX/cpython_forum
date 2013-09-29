from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cpython_forum.views.index', name='home'),
    # url(r'^cpython_forum/', include('cpython_forum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/',include('grappelli.urls')),
    (r'^static/(?P<path>.*)$','django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT , 'show_indexes':True}),
    (r'^node/index/$','cpython_forum.views.node_index'),
    (r'^say/(\d+)/$','cpython_forum.views.say'),
    (r'^delete/(\d+)/$','cpython_forum.views.delete_list'),
    (r'^update/(\d+)/$','cpython_forum.views.update'),
    (r'^upload/$', 'cpython_forum.views.upload'),
    (r'^member/(.*)/$','cpython_forum.views.usercenter'),
    (r'^users/$','cpython_forum.views.users'),
    (r'^about/$','cpython_forum.views.about'),
    (r'^messages/$',include('messages.urls')),
    (r'^message/$','cpython_forum.views.gonggao'),
    (r'^gegeda/$','cpython_forum.views.index_gegeda'),
    (r'^uploadchange/$','cpython_forum.views.uploadchange'),
    (r'^sendmessages/add/$','cpython_forum.views.sendmessages_add'),
    (r'^sendmessages/save/$','cpython_forum.views.sendmessages_save'),

)

urlpatterns += patterns('',
	 (r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
	 (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
	 (r'^accounts/register/$', 'cpython_forum.views.register'),
)
urlpatterns += patterns('',
	 (r'^nodecate/add/$', 'cpython_forum.node_views.nodecate_add'),
	 (r'^nodecate/save$', 'cpython_forum.node_views.nodecate_save'),
	 (r'^node/add/(\d+)$', 'cpython_forum.node_views.node_add'),
	 (r'^node/save$', 'cpython_forum.node_views.node_save'),
	 (r'^node/article/$','cpython_forum.node_views.topic_add'),
	 (r'^topic/save$','cpython_forum.node_views.topic_save'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT}))
