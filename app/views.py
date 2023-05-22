from django.shortcuts import render,redirect
from . models import *
# Create your views here.


#index file view
def IndexPage(request):
    return render(request,"app/index.html")


# Upload image
def Uploadimage(request):
    if request.method == "POST":
        imagename = request.POST['imgname']
        pics = request.FILES['image'] # Use request.FILES to access the uploaded file
        newimg = ImageData.objects.create(Imagename=imagename, Image=pics)
        return redirect("show")
        

#Image feching View
def ImageFetch(request):
    all_img = ImageData.objects.all()
    return render(request, "app/Show.html", {'key1': all_img})
