from django.conf.urls import url
from template_app import views

#Template Tagging
app_name = 'template_app'

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^other/$', views.other, name='other'),
    url(r'^relative/$', views.relative, name='relative'),
]
