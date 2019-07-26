from django.shortcuts import render
from django.http import HttpResponse
from pages.models import ContactModel
from django.http import HttpResponseRedirect
# Create your views here.
def Home(request):
    return render(request,'index.html',{'title': 'Home Page Title'})
    
def Contact(request):

    if request.method=='GET' and request.GET.get('method') == 'delete':
        rec = ContactModel.objects.filter(id = request.GET.get('id'))
        rec.delete()
    
    if request.method=='GET' and  request.GET.get('method') == 'edit':
        cnt = ContactModel.objects.filter(id = request.GET.get('id')).get()
        return render(request,'edit.html',{'title': 'Contact Page Title','row':cnt})
   
        
    if request.method=='POST':

        if request.GET.get('method') =='update':
            rec = ContactModel.objects.filter(id=request.GET.get('id'))
            rec.update(
            firstname = request.POST['name'],
            lastname = request.POST['lastname'],
            email = request.POST['email'],
            message = request.POST['message']
            )
            return HttpResponseRedirect('/contact/')
        else:
            data=ContactModel(
                firstname = request.POST['name'],
                lastname = request.POST['lastname'],
                email = request.POST['email'],
                message = request.POST['message']
            )
            data.save()
        #name= request.POST['name']
        #lastname = request.POST['lastname']
        #message = request.POST['message']
        #email=request.POST['email']

    cnt = ContactModel.objects.all()
        #return render(request,'contact.html',{'title': 'Contact Page Title','name':name,'lastname':lastname,'message':message})
    return render(request,'contact.html',{'title': 'Contact Page Title','rows':cnt})

def About(request):
    return render(request,'about.html',{'title': 'About Page Title'})

def team(request):
    #return HttpResponse(request.Get.get('cat_id'))
    if(request.method == 'Get' and 'cat_id' in request.Get and 'mem_id' in request.Get):
        return HttpResponse('<h1> Team Members id {} form category id {}<h1>'.format(request.Get.get('mem_id'),request.Get.get('cat_id')))
    else:
        return HttpResponse("<h1> Team Member List</h1>")