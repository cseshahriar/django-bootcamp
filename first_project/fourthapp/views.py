from django.shortcuts import render 

# Create your views here.
def index(request):
    my_dictionary = {"content": "Hello I am from fourthapp!"}
    return render(request, 'fourthapp/index.html', my_dictionary)  