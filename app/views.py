from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader
from app.models import JobPost

job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]

job_description=[
    "First job description",
    "Second job description",
    "Third job description",
]

# Create your views here.
def job_list(request):
    jobs = JobPost.objects.all()
    context = {"jobs":jobs}
    return render(request, 'app/job_list.html', context)

def job_detail(request, id):
    try:
        if id==0:
            return redirect(reverse('jobs_home'))
        
        job = JobPost.objects.get(id=id)
        print(job)
        context = {"job":job}
        return render(request, 'app/job_detail.html', context)
    except:
        # this will return a 404 not found response with the text specified in the method
        return HttpResponseNotFound("Not Found")
    
    
class TempClass:
    x = 5

def hello(request):
    template = 'app/hello.html'
    list = ["alpha", "beta"]
    temp = TempClass()
    is_authenticated = False
    # create context
    context = {"name":"django", "first_list":list, "temp_object":temp,"age":28, "is_authenticated": is_authenticated}
    # return response
    return render(request, template, context)