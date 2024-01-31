from django.shortcuts import render
from uploadapp.forms import UploadForm, UploadFileForm

# Create your views here.
def upload_image(request):
    if request.method=="POST":
        # get post data and all the files
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            saved_object = form.instance
            return render(request, 'uploadapp/add_image.html', {'form':form, 'saved_object':saved_object})   
    else:
        form = UploadForm()
    return render(request, 'uploadapp/add_image.html', {'form':form})   

def upload_file(request):
    if request.method=="POST":
        # get post data and all the files
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            saved_object = form.instance
            return render(request, 'uploadapp/add_file.html', {'form':form, 'saved_object':saved_object})   
    else:
        form = UploadFileForm()
    return render(request, 'uploadapp/add_file.html', {'form':form})   