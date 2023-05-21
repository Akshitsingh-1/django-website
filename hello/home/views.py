from datetime import datetime
from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable1":"Akshit is great",
        "variable2":"Akshu is great"
    }
    #messages.success(request,"This is a Text Message")
    return render(request,'index.html',context)
    #return HttpResponse("This is Homepage")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is about")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is services")

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your Message have been sent!')
    return render(request,'contact.html')

    #return render(request,'contact.html')
    #return HttpResponse("This is contact")