from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework import parsers

from .models import Image
from .serializers import ImageSerializer


class ImageView(CreateAPIView):

    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (parsers.MultiPartParser,)
from django.shortcuts import render
from .forms import ImageForm








