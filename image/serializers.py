from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Image
import os
import cv2
import sys

from django.core.files.base import ContentFile

from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('title','image')

    def validate_image(self,Image):
        image=Image['image']
        url=os.path.join(settings.TEMP,str(image))
        storage=FileSystemStorage(location=url)
        with storage.open('','wb+') as destionation:
            for chunk in image.chunks():
                destionation.write(chunk)
            destionation.close()

        im=cv2.imread(url)

        text = "image"
        if str(im).endswith(".jpg") or str(im).endswith(".png"):



            # load the image, convert it to grayscale, and compute the
            # focus measure of the image using the Variance of Laplacian
            # method
            image = cv2.imread(cv2.samples.findFile(im), cv2.IMREAD_COLOR)
            # image = cv2.GaussianBlur(image, (3, 3), 0)
            # image = cv2.imread(img)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            fm = cv2.Laplacian(gray, cv2.CV_64F).var()

            # if the focus measure is less than the supplied threshold,
            # then the image should be considered "blurry"
            if fm < 1500:
                text = "Blurry"
            # show the image
        return text


    '''title = Image.title(validators=[
           UniqueValidator(
               queryset=Image.objects.all(),
               message='Such email address already exists'
           )]
       )'''
    '''def aavalidate(self,Image):
        image=Image['image']
        url=os.path.join(settings.TEMP  , str(image))
        storage=FileSystemStorage(location=url)
        if storage.endwith('png'):
            pass
        with storage.open('','wb+') as destination:
            if destination!=0:
                pass

    def variance_of_laplacian(self,Image):
        # compute the Laplacian of the image and then return the focus
        # measure, which is simply the variance of the Laplacian
        # return cv2.Laplacian(image, cv2.CV_64F).var()
        # construct the argument parse and parse the arguments
        image=Image['image']
        url=os.path.join(settings.TEMP  , str(image))
        image=FileSystemStorage(location=url)
        text = 'not Blurry'
        if image.endswith(".jpg") or image.endswith(".png"):

            # load the image, convert it to grayscale, and compute the
            # focus measure of the image using the Variance of Laplacian
            # method
            image = cv2.imread(cv2.samples.findFile(image), cv2.IMREAD_COLOR)
            # image = cv2.GaussianBlur(image, (3, 3), 0)
            # image = cv2.imread(img)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            fm = cv2.Laplacian(gray, cv2.CV_64F).var()

            # if the focus measure is less than the supplied threshold,
            # then the image should be considered "blurry"
            if fm < 1500:
                text = "Blurry"
            # show the image

        return text'''
