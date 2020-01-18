from django.conf.urls import url

from . import views

app_name = 'cpa_api'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^generate/(\d+)/$', views.get_points, name='points'),
    url(r'^generate/(?P<string>[\w\-]+)/$', views.generate, name='quick_hull'),
    url(r'^generate/quickhull/$', views.quickHull, name='quick_hull'),
    url(r'^generate/quickhull/(?P<string>[\w\-]+)/$', views.quickHull, name='ritter'),
    url(r'^generate/ritter/$', views.ritter, name='index'),
    url(r'^generate/ritter/(?P<string>[\w\-]+)/$', views.ritter, name='ritter'),
    url(r'^generate/envloppe_convexe/$', views.convexe, name='convexe'),
    url(r'^generate/envloppe_convexe/(?P<string>[\w\-]+)/$', views.convexe, name='convexe'),

]
