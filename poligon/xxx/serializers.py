from rest_framework import serializers
from .models import SiteImages, Domain
from rest_framework.validators import UniqueTogetherValidator


class DomainSerializer(serializers.ModelSerializer):
    images = serializers.HyperlinkedIdentityField(view_name='xxx:image-list', lookup_url_kwarg='domain_id')
    class Meta:
        model = Domain
        fields = '__all__'


# class SiteImagesSerializer(serializers.Serializer):
#     image_url = serializers.CharField()
#     page_width = serializers.IntegerField()
#     page_height = serializers.IntegerField()


class SiteImagesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='xxx:image-detail',lookup_url_kwarg='image_id')
    load_orig = serializers.HyperlinkedIdentityField(view_name='xxx:image-load-orig', lookup_url_kwarg='image_id')
    make_thumb = serializers.HyperlinkedIdentityField(view_name='xxx:image-make-thumb', lookup_url_kwarg='image_id')
    load_make_thumb = serializers.HyperlinkedIdentityField(view_name='xxx:load-make-thumb', lookup_url_kwarg='image_id')
    class Meta:
        model = SiteImages
        fields = '__all__'
        extra_kwargs = {
            'orig_img': {'read_only': True},
            'thumb_img': {'read_only': True},
        }
        validators = [
            UniqueTogetherValidator(
                queryset=SiteImages.objects.all(),
                fields=['domain', 'image_url']
            )
        ]
