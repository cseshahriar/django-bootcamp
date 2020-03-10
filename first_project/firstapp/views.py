from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        'insert_me' : 'lorem ipsum'
    }
    return render(request, 'firstapp/index.html', data)   
