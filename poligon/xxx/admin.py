from django.contrib import admin
from .models import Domain, SiteImages, ImageEx


def load_image(modeladmin, request, queryset):
    for model in queryset:
        model.load_orig_img(soft=True)


class SiteImagesAdmin(admin.ModelAdmin):
    list_display = ['id','domain','image_url','orig_img','thumb',]

    actions = [load_image, 'make_thumb', 'delete_images']

    @admin.action(description='Make Thumb')
    def make_thumb(self, request, queryset):
        for m in queryset:
            m.make_thumb()

    @admin.action(description='Delete images')
    def delete_images(self, request, queryset):
        for m in queryset:
            m.delete_images()


admin.site.register(Domain)
admin.site.register(SiteImages, SiteImagesAdmin)
admin.site.register(ImageEx)