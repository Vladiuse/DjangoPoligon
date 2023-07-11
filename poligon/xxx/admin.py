from django.contrib import admin
from .models import Domain, SiteImages, ImageEx
from django.utils.html import mark_safe
import re


def img_tag(src):
    return mark_safe(f'<img src="{src}" width="50px" height="50px" />')


def remove_protokol(url: str):
    return re.sub('http[s]?://', '', url)


def load_image(modeladmin, request, queryset):
    for model in queryset:
        model.load_orig_img(soft=True)


class SiteImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'domain', 'image_url_short', 'orig_img', 'orig_tag', 'thumb', 'thumb_tag']
    actions = [load_image, 'make_thumb', 'delete_images']

    @admin.action(description='Make Thumb')
    def make_thumb(self, request, queryset):
        for m in queryset:
            m.make_thumb()

    @admin.action(description='Delete images')
    def delete_images(self, request, queryset):
        for m in queryset:
            m.delete_images()

    def image_url_short(self, obj):
        return remove_protokol(obj.image_url)

    def orig_tag(self, obj):
        if obj.orig_img:
            return img_tag(obj.orig_img.url)

    def thumb_tag(self, obj):
        if obj.thumb:
            return img_tag(obj.thumb.url)


admin.site.register(Domain)
admin.site.register(SiteImages, SiteImagesAdmin)
admin.site.register(ImageEx)
