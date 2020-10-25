from django.shortcuts import render
from rest_framework import status
# Create your views here.
from rest_framework.generics import ListCreateAPIView
from rest_framework import parsers
from rest_framework.decorators import api_view
import requests
from django.contrib import messages
from .models import Image
from rest_framework.request import Request
from django.utils.text import slugify
from .forms import ImageForm
from .serializers import ImageSerializer
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.messages import constants as messages
class ImageView(ListCreateAPIView):

    '''queryset = Image.objects.all()'''
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (parsers.MultiPartParser,)

    '''def ImageCreate(request):
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES['image'])
            if form.is_valid():
                image = form.save(commit=False)

                image.save()
                messages.success(request, "Uploaded successfully")
                return redirect('mytimer')
            else:
                messages.error(request, "Unable to upload at this time")

        else:
             form = ImageForm()


        return render(request, "myimages.html", {'form': form})'''

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        a=1
        if a==1:
            return Response({
            'status': 200,
            'message': 'Testimonials fetched',
            'data': response.data["image"]

        })
        else:
            return Response({
                "a is not equal to 1"
            })

    def api_uploadimage(self,request):
        serializer=ImageSerializer(Image,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['response']=UPDATE_SUCCESS




    '''def detectiongImageIFBlur(self,request):
        image=Image.objects.get("image")
        serilizer=ImageSerializer(image)
        if serilizer=='Blurry':
            return Response("blurry images are invalid")
            

    def renew_book_librarian(self,request, pk):
        book_instance = get_object_or_404(Image, pk=pk)
    
        # If this is a POST request then process the Form data
        if request.method == 'POST':

            # Create a form instance and populate it with data from the request (binding):
            form = ImageForm(request.POST)

            # Check if the form is valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
                book_instance.due_back = form.cleaned_data['renewal_date']
                book_instance.save()

                # redirect to a new URL:
                return HttpResponseRedirect(reverse('all-borrowed'))

        # If this is a GET (or any other method) create the default form.
        else:
            proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
            form = ImageForm(initial={'renewal_date': proposed_renewal_date})

        context = {
            'form': form,
            'book_instance': book_instance,
        }

        return render(request, 'index.html', context)'''








