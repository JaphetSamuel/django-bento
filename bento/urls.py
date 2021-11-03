from django.urls import path

pref='bento.views'
urlpatterns = [
    path(r'^image-upload/$', f'{pref}.image_upload', name='bento-image-import'),
    path(r'^text-upload/$', f'{pref}.text_upload', name='bento-text-import'),
    path(r'^text-edit/(?P<name>[\w-]+)/$', f'{pref}.text_edit', name='bento-text-edit'),
    path(r'^image-edit/(?P<name>[\w-]+)/$', f'{pref}.image_edit', name='bento-image-edit'),
]
