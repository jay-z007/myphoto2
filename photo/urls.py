__author__ = 'Jay'

from django.conf.urls import url, patterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^albums/$', views.albums, name='albums'),
    url(r'^login/$', views.login_form, name='login'),
    url(r'^register/$', views.register_form, name='register'),
    url(r'^user/logout/$', views.logout_view, name='logout'),
    url(r'^success/(?P<album_id>[0-9]+)/$', views.success, name='success'),
    url(r'^search/$', views.search, name='search'),
    url(r'^user/edit/$', views.user_update, name="user_update"),
    url(r'^(?P<photo_id>[0-9]+)/$', views.photo_detail, name='photo_detail'),
    url(r'^forgot-password/$', views.forgot_password, name='forgot_password'),
    url(r'^albums/(?P<album_id>[0-9]+)/$', views.album_details, name='album_details'),
    url(r'^upload/$', views.upload_photo, name='upload_form'),
    url(r'^create_album/$', views.create_album, name='create_album'),
    url(r'^albums/(?P<album_id>[0-9]+)/slide-show/$', views.slide, name='slide'),
    url(r'^albums/photo-booth-strips/$', views.photo_booth_strips, name='photo_booth_strips'),
    url(r'^developers/$', views.dev, name='dev'),
    url(r'^about-us/$', views.abt, name='abt'),
   ]

# urlpatterns += patterns('',
#     url(
#         regex=r'^(?P<pk>\d+)/ajax-upload/$',
#         view=views.AjaxPhotoUploadView.as_view(),
#         name='ajax_photo_upload_view',
#     ),
# )