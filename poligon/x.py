import os
from PIL import Image
import io
from PIL import Image
from django.core.files.images import ImageFile
from xxx.models import SiteImages

DIR_PATH = '/home/vlad/WORK'
BMP_PATH = os.path.join(DIR_PATH, 'BMP.bmp')
JPEG_PATH = os.path.join(DIR_PATH, 'JPEG.jpeg')
JPG_PATH = os.path.join(DIR_PATH, 'JPG.jpg')
PNG_PATH = os.path.join(DIR_PATH, 'PNG.png')
WEBP_PATH = os.path.join(DIR_PATH, 'WEBP.webp')


BMP = Image.open(BMP_PATH)
JPEG = Image.open(JPEG_PATH)
JPG = Image.open(JPG_PATH)
PNG = Image.open(PNG_PATH)
WEBP = Image.open(WEBP_PATH)


for image in [BMP,JPEG, JPG, PNG, WEBP]:
    print(image.format)

image_model = SiteImages.objects.get(pk=66)