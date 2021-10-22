from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('blog/', include('blog.urls')),
    path('register/', user_views.register, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
