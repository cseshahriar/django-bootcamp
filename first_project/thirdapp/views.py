from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict =  {'insert_content':'Hello I am from thirdap'}
    return render(request, 'thirdapp/index.html', my_dict)  