from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="crm api ",
        default_version='v1',
        description="docs for project",
        contact=openapi.Contact(email="nurga1997@gmail.com"),
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/crm/', include('crm.urls')),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
