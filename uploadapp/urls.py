from django.urls import path
from uploadapp.views import upload_image, upload_file

urlpatterns = [
    path('image', upload_image, name="upload_image"),
    path('file', upload_file, name="upload_file"),
]