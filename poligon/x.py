# import os
# from PIL import Image
# import io
# from PIL import Image
# from django.core.files.images import ImageFile
# from xxx.models import SiteImages
#
# DIR_PATH = '/home/vlad/WORK'
# BMP_PATH = os.path.join(DIR_PATH, 'BMP.bmp')
# JPEG_PATH = os.path.join(DIR_PATH, 'JPEG.jpeg')
# JPG_PATH = os.path.join(DIR_PATH, 'JPG.jpg')
# PNG_PATH = os.path.join(DIR_PATH, 'PNG.png')
# WEBP_PATH = os.path.join(DIR_PATH, 'WEBP.webp')
#
#
# BMP = Image.open(BMP_PATH)
# JPEG = Image.open(JPEG_PATH)
# JPG = Image.open(JPG_PATH)
# PNG = Image.open(PNG_PATH)
# WEBP = Image.open(WEBP_PATH)
#
#
# for image in [BMP,JPEG, JPG, PNG, WEBP]:
#     print(image.format)
#
# image_model = SiteImages.objects.get(pk=66)

from xxx.models import Domain, SiteImages
from xxx.serializers import SiteImagesSerializer

domain = Domain.objects.get(pk=1)
data = {
    'domain': 1,
    'image_url': 'https://kartinkof.club/uploads/posts/2022-05/1652654546_1-kartinkof-club-p-prikoli-o-subbote-kartinki-1.jpg',
    'page_width': 30,
    'page_height': 30,
}

serializer = SiteImagesSerializer(data=data)