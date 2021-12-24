from . import views
from django.urls import path


urlpatterns = [
    path('image-upload/', views.image_upload, name='bento-image-import'),
    path('text-upload/', views.text_upload, name='bento-text-import'),
    path('text-edit/<str:name>/', views.text_edit, name='bento-text-edit'),
    path('image-edit/<nstr:ame>/', views.image_edit, name='bento-image-edit'),
]
