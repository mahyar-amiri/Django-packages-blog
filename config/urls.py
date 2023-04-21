from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls')),
    path('comment/', include('comment.urls')),
    path('rating/', include('rating.urls')),
    path('reaction/', include('reaction.urls')),

    path('panel/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'blog.views.error_404'
