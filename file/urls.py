from django.conf.urls import url
from . import views
app_name='file'
urlpatterns = [
  url(r'^form/$', views.postlist1, name='postlist1'),
  url(r'^form/info/$', views.info, name='info'),
  url(r'^form/info/search/$',views.search,name='search'),
  url(r'^form/info/sort/$',views.sort,name='sort')
]
