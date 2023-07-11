from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from .models import Question, SiteImages, Domain, ImageEx
from .img_info import get_image_info
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, action
from .serializers import SiteImagesSerializer, DomainSerializer
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

class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

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

    @action(detail=True, methods=['GET'])
    def load_orig(self, request,image_id):
        obj = self.get_object()
        obj.load_orig_img()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def make_thumb(self, request,image_id):
        obj = self.get_object()
        obj.make_thumb()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def load_make_thumb(self, request,image_id):
        obj = self.get_object()
        res = obj.load_make_thumb()
        serializer = self.get_serializer(obj)
        return Response({
            'result': res,
            'image': serializer.data
        })


    # def get_object(self):
    #     print('get_object')
    #     print(self.kwargs)
    #     return SiteImages.objects.get(domain_id=self.kwargs['domain_id'], pk=self.kwargs['image_id'])
