from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'domains', views.DomainViewSet)

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

site_image_load = views.SiteImagesViewSet.as_view({
    'get': 'load_orig'
})
make_thumb = views.SiteImagesViewSet.as_view({
    'get': 'make_thumb'
})

load_make_thumb = views.SiteImagesViewSet.as_view({
    'get': 'load_make_thumb'
})

app_name = 'xxx'
urlpatterns = [
    path('', views.index, name='index'),
    path('checker_2/get-img-info/', views.image_info),
    path('domains/<int:domain_id>/site-images/', site_images_list, name='image-list'),
    path('site-images/<int:image_id>/', site_images_detail, name='image-detail'),
    path('site-images/<int:image_id>/load-orig/', site_image_load, name='image-load-orig'),
    path('site-images/<int:image_id>/make-thumb/', make_thumb, name='image-make-thumb'),
    path('site-images/<int:image_id>/load-make-thumb/', load_make_thumb, name='load-make-thumb'),
    path('', include(router.urls)),
]