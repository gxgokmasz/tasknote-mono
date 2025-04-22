from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path("admin/", admin.site.urls),
    path("", include("modules.authentication.src.presentation.urls")),
    path("", include("modules.tasks.src.presentation.urls")),
    # path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
