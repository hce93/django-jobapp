from django.db import models

# Create your models here.
class Uploads(models.Model):
    # we need to add an upload_to to tell django whre to store the files
    image = models.ImageField(upload_to="images")
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.description
    
class UploadFile(models.Model):
    file = models.FileField(upload_to="files")
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.description