from . import views
from django.urls import path


urlpatterns = [
    path(r'^image-upload/$', views.image_upload, name='bento-image-import'),
    path(r'^text-upload/$', views.text_upload, name='bento-text-import'),
    path(r'^text-edit/(?P<name>[\w-]+)/$', views.text_edit, name='bento-text-edit'),
    path(r'^image-edit/(?P<name>[\w-]+)/$', views.image_edit, name='bento-image-edit'),
]
