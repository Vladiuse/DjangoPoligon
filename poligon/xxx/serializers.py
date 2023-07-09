from rest_framework import serializers
from .models import SiteImages


# class SiteImagesSerializer(serializers.Serializer):
#     image_url = serializers.CharField()
#     page_width = serializers.IntegerField()
#     page_height = serializers.IntegerField()


class SiteImagesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='xxx:image-detail',lookup_url_kwarg='image_id')
    class Meta:
        model = SiteImages
        fields = '__all__'
        extra_kwargs = {
            'orig_img': {'read_only': True},
            'thumb_img': {'read_only': True},
            'image_url': {'read_only': True},
        }
