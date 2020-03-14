from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request):
    # return HttpResponse('Test') #ok
    context_dict = {'text': 'Hello World', 'number':100}
    return render(request, 'basicapp/index.html', context_dict)   
    

def others(request):
    return render(request, 'basicapp/others.html') 