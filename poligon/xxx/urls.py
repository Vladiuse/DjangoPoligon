from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'images', views.SiteImagesViewSet,
#                 basename='info')

site_images_list = views.SiteImagesViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

site_images_detail = views.SiteImagesViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

app_name = 'xxx'
urlpatterns = [
    path('', views.index, name='index'),
    path('get-img-info', views.image_info),
    path('domain/<int:domain_id>/site-images/', site_images_list, name='image-list'),
    path('site-images/<int:image_id>/', site_images_detail, name='image-detail'),
    # path('domain/<int:domain_id>/', include(router.urls)),
]