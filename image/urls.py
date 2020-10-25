from django.urls import path
from .views import ImageView
from image import views
urlpatterns = [
path('', ImageView.as_view(), name='image'),

]