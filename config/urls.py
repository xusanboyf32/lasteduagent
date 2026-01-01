
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# ---------------- Swagger sozlamalari ----------------
schema_view = get_schema_view(
    openapi.Info(
        title="Education Platform API",
        default_version="v1",
        description="Professional API documentation",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# ---------------- Asosiy URL Config ------------------
urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication (masalan JWT yoki DRF auth)
    path('api/auth/', include('rest_framework.urls')),

    # COURSE app uchun API
    path('api/course/', include(('course.urls', 'course'), namespace='course')),

    # STUDENT app uchun API
    path('api/student/', include(('student.urls', 'student'), namespace='student')),

    # Swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('ai/', include('chatai.urls')),

]


# media yuklangan media chiqishi uchun
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

