
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from libros.views import LibroViewSet,prestamos_semana

router = DefaultRouter()
router.register(r'libros', LibroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('prestamos/semana', prestamos_semana),
]
