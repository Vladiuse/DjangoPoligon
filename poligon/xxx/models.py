import os.path

from django.db import models
from datetime import timedelta
from django.utils import timezone
import requests as req
from requests.exceptions import RequestException
from django.core.files import File
import io
from PIL import Image
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import Manager

def load_img_http(url):
    result = {}
    try:
        res = req.get(url)
        if res.status_code == 200:
            result['status'] = True
            result['content'] = res.content
        else:
            result['status'] = False
            result['msg'] = 'status code ' + str(res.status_code)
    except RequestException as error:
        result['status'] = False
        result['msg'] = 'status code ' + str(error)
    return result


def make_thumb(image_path, size:tuple, compress=False):
    image = Image.open(image_path)
    image.thumbnail(size)
    return image



class Question(models.Model):
    pub_date = models.DateField()
    text = models.CharField(max_length=50)

    def was_published_recently(self):
        if timezone.now().date() >= self.pub_date >= (timezone.now().date() - timedelta(days=1)):
            return True
        return False

    class Meta:

        ordering = ['-pk']


class Book(models.Model):
    price = models.FloatField(default=0)


class ImageEx(models.Model):
    image = models.ImageField(upload_to='examples')

    class Meta:
        verbose_name = 'Заготовка картинки'
        verbose_name_plural = 'Заготовки картинок'

    def __str__(self):
        return self.image.name


class Domain(models.Model):
    name = models.URLField(unique=True)

    def __str__(self):
        return self.name


def image_path(instanse, filename):
    domain_name = instanse.domain.name.replace('http://','')
    return f'{domain_name}/{filename}'

class SiteImages(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    image_url = models.URLField()
    page_width = models.IntegerField()
    page_height = models.IntegerField()
    orig_img = models.ImageField(blank=True, upload_to=image_path,)
    thumb = models.ImageField(blank=True,upload_to=image_path, )
    thumb_compress = models.ImageField(blank=True,upload_to=image_path, )

    class Meta:
        unique_together = ['domain', 'image_url']
        ordering = ['-pk']

    def delete_images(self):
        for field in self.orig_img, self.thumb:
            if field:
                if os.path.exists(field.path):
                    os.remove(field.path)
        self.orig_img = None
        self.thumb = None
        self.save()


    def load_orig_img(self, soft=False):
        if soft and self.orig_img:
            return
        print('lOAD')
        res = load_img_http(self.image_url)
        if res['status']:
            bytes = res['content']
            ext = os.path.splitext(self.image_url)[1]
            img = ImageFile(io.BytesIO(bytes), name=f'some{ext}')
            self.orig_img = img
            self.save()
            print(res['status'])
        else:
            print(res)
            return res

    def ext(self):
        return os.path.splitext(self.orig_img.path)[1]

    def make_thumb(self):
        size = (self.page_width,self.page_height)
        thumb = make_thumb(self.orig_img.path, size)
        blob = io.BytesIO()
        thumb.save(blob, thumb.format)
        ext = os.path.splitext(self.image_url)[1]
        self.thumb = ImageFile(blob, name=f'THUMB{ext}')
        self.save()

    def load_make_thumb(self):
        res_loading = self.load_orig_img()
        if res_loading['status']:
            self.make_thumb()
        return res_loading

    def compression_percent(self):
        if self.orig_img and self.thumb:
            return round(self.orig_img.size/self.thumb.size/100, 1)

    def compression_weight(self):
        if self.orig_img and self.thumb:
            return self.orig_img.size - self.thumb.size


