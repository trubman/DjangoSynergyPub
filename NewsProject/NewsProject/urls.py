from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from NewsProject.settings import STATIC_URL, STATIC_ROOT
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('News.urls')),
    path('homework/', include('Homework.urls')),
    path('reg/', include('Register.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('captcha/', include('captcha.urls')),
] # + debug_toolbar_urls()

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()
    # import debug_toolbar
    # urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
