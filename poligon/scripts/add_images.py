from xxx.models import Domain, ImageEx,SiteImages

SiteImages.objects.all().delete()
domain = Domain.objects.get(pk=1)
for i in ImageEx.objects.all():
    url = 'http://127.0.0.1:8000' + i.image.url
    SiteImages.objects.create(domain=domain, image_url=url)