from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, 'form/index.html')


# generate a form view  
def form_name_view(request):
    form = forms.FormName() # instance of FormName class 

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # do something code
            print('Validation Success!')
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text']) 

    return render(request, 'form/form_page.html', {'form':form})
 