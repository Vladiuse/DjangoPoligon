from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from .models import Question, SiteImages, Domain, ImageEx
from .img_info import get_image_info
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import SiteImagesSerializer
from rest_framework.response import Response
import json
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from shell import *

def index(request):
    docs = Question.objects.all()
    images = ImageEx.objects.all()
    site_images = SiteImages.objects.all()
    content = {
        'docs': docs,
        'text': 'Some text',
        'site_images':site_images,
        'images': images,
    }
    return render(request, 'xxx/index.html', content)



@csrf_exempt
@require_http_methods(['POST'])
def image_info(request):
    print(request.POST)
    img_href = request.POST['img_href']
    info = get_image_info(img_href)
    return JsonResponse(info, safe=True)


class SiteImagesViewSet(viewsets.ModelViewSet):
    serializer_class = SiteImagesSerializer

    lookup_field = 'image_id'
    lookup_url_kwarg = 'image_id'

    def domain(self):
        return Domain.objects.get(pk=self.kwargs['domain_id'])

    def get_queryset(self):
        return SiteImages.objects.filter(domain_id=self.kwargs['domain_id'])

    def get_object(self):
        return SiteImages.objects.get(pk=self.kwargs['image_id'])

    # def get_object(self):
    #     print('get_object')
    #     print(self.kwargs)
    #     return SiteImages.objects.get(domain_id=self.kwargs['domain_id'], pk=self.kwargs['image_id'])
