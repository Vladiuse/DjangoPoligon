from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

site_images_list = views.SiteImagesViewSet.as_view({
    'get': 'list',
})
router = DefaultRouter()
router.register(r'', views.SiteImagesViewSet,
                basename='info')
app_name = 'xxx'
urlpatterns = [
    path('', views.index, name='index'),
    path('q/<int:question_id>', views.get_q, name='get_q'),
    path('test', views.test, name='test'),
    path('get-img-info', views.image_info),
    path('images_info/<int:domain_id>/', site_images_list),
    path('images_info_2/<int:domain_id>/', include(router.urls)),
]