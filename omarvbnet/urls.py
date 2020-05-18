
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jops.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jops.views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('jops/', include('jops.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
