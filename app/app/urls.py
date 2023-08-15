
from django.contrib import admin
from django.urls import path, include

from django.conf import settings#追加
from django.conf.urls.static import static#追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
]+ static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#↑画像のパスとかを教えてる（#追加）
