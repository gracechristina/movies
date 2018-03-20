from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^movie/admin/newmovie/$', views.movie_new, name="movie_new"),
    url(r'^movie/admin/newcinema/$', views.theatre_new, name="theatre_new"),
    url(r'^movie/(?P<pk>\d+)/$', views.movie_detail, name="movie_detail"),
    url(r'^$', views.movie_list, name="movie_list"),
    url(r'^movie/admin',views.admin, name="admin"),
    url(r'^movie/booking',views.booking, name="booking"),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name="post_detail"),
    url(r'^post/new/$', views.post_new, name="post_new"),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name="post_edit"),
    url(r'^drafts/$', views.post_draft_list, name="post_draft_list"),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name="post_publish"),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name="post_remove"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

