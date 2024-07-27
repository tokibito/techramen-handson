from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('self_order.urls')),  # self_orderのURLを有効化
]
urlpatterns += debug_toolbar_urls()  # django-debug-toolbar
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # アップロードファイル