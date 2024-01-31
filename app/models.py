from django.db import models
from django.utils.text import slugify

# Create your models here.

# this model will have a one-to-one relationship (one loacation to one jobpost)
class Location(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
   
# this model will have a many to one relationship (many jobpost to one author)
class Author(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    
# this model will have a many-to-many relationship with JobPost
class Skills(models.Model):
    name = models.CharField(max_length=200)
    
 
class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time')
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    expiry = models.DateField(null=True)
    salary = models.IntegerField()
    # allow null values in the slug field as we will generate this when object is saved
    slug = models.SlugField(null=True, max_length=40, unique=True) 
    # create one-to-one relationship. Cascade deletions when job post is deleted
    location = models.OneToOneField(Location, on_delete=models.CASCADE ,null=True)
    # Create many-to-one relationship. JobPost to one author
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skills)
    type = models.CharField(max_length=200, null=False, choices=JOB_TYPE_CHOICES)
    
    #override the save method so we can create the slug field 
    def save(self, *args, **kwargs):
        # check if id doesn't exist. If it doesnt then geenrate the slug
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} with salary {self.salary:,}"
    

    