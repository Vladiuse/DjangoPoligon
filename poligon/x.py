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
import os.path

from django.db import models
from datetime import timedelta
from django.utils import timezone
import requests as req
from requests.exceptions import RequestException
import io
from PIL import Image
from django.core.files.images import ImageFile

def load_img_http(url):
    result = {}
    result['status'] = False
    try:
        res = req.get(url)
        if res.status_code != 200:
            result['msg'] = 'status code ' + str(res.status_code)
        elif res.headers['Content-Type'] and not res.headers['Content-Type'].startswith('image'):
            result['msg'] = res.headers['Content-Type']
        else:
            result['status'] = True
            result['content'] = res.content
    except RequestException as error:
        result['msg'] = 'status code ' + str(error)
    return result
url = 'http://amazing-cdn.com/e.wloss-new.com/graziani_files/logo.png'

print(load_img_http(url))