# from django.contrib import admin
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
from django.contrib import admin
from django.urls import include, path, re_path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from fusion import views
from fusion.views import *

# from fusion.views import FileUploadAPIView
from usuario.router import router as usuario_router

# from fusion.views import export_data_to_excel, import_data_to_excel


app_name = "api"

router = router = DefaultRouter()
urlpatterns = [
    path("export_data_to_excel/", export_data_to_excel),
    path("import_data_to_excel/", import_data_to_excel),
    path("admin/", admin.site.urls),
    # path("api/", include(router.urls)),
    # path("api/", include(usuario_router.urls)),
    # path("", views.simple_upload),
    # path("test", views.TestView.as_view(), name="test"),
    # re_path(r"^upload/(?P<filename>[^/]+)$", FileUploadView.as_view()),
    # path("test", views.test, name="test"),
    # path("upload-file/", FileUploadAPIView.as_view(), name="upload-file"),
    # path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # path(
    #     "api/swagger/",
    #     SpectacularSwaggerView.as_view(url_name="schema"),
    #     name="swagger-ui",
    # ),
    # path(
    #     "api/redoc/",
    #     SpectacularRedocView.as_view(url_name="schema"),
    #     name="redoc",
    # ),
]
