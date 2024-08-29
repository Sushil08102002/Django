from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from tutorial1.quickstart import views
from django.conf import settings
from django.conf.urls.static import static

router=routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('api/v1/',include('API.urls')),
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
