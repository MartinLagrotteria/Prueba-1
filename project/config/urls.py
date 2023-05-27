from django.contrib import admin
from django.urls import include, path




urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("home.urls", "home"))),
     path("", include(("venta.urls", "venta"))),
    path("libros/", include(("libros.urls", "libros"))),


]

