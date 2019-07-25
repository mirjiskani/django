from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return render(request,'index.html',{'title': 'Home Page Title'})
    
def Contact(request):
    if request.method=='POST':
        name= request.POST['name']
        lastname = request.POST['lastname']
        message = request.POST['message']
        return render(request,'contact.html',{'title': 'Contact Page Title','name':name,'lastname':lastname,'message':message})
    return render(request,'contact.html',{'title': 'Contact Page Title'})

def About(request):
    return render(request,'about.html',{'title': 'About Page Title'})

def team(request):
    #return HttpResponse(request.Get.get('cat_id'))
    if(request.method == 'Get' and 'cat_id' in request.Get and 'mem_id' in request.Get):
        return HttpResponse('<h1> Team Members id {} form category id {}<h1>'.format(request.Get.get('mem_id'),request.Get.get('cat_id')))
    else:
        return HttpResponse("<h1> Team Member List</h1>")