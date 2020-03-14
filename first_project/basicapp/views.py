from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request):
    # return HttpResponse('Test') #ok
    return render(request, 'basicapp/index.html')  
    

def others(request):
    return render(request, 'basicapp/others.html') 