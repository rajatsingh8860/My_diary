from django.shortcuts import render,redirect
from .models import Input
from .forms import Entryform

# Create your views here.
def index(request):
    inputs=Input.objects.all()
    feed={'inputs':inputs}
    return render(request,'day_to_diary/index.html',feed)

def add(request):
    if request.method=='POST':
        form=Entryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:    
        form=Entryform()

    feed={'form':form}
    return render(request,'day_to_diary/add.html',feed)    
