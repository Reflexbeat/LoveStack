from django.urls import path
from .views import IndexView, message_text ,preview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', IndexView.as_view(), name='index'),
    path('message/',message_text, name='create_message'),
    path('preview/<slug:slug>/',preview, name='preview')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)