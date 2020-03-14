from django.shortcuts import render
from apptwo.forms import NewUserForm


def index(request):
    return render(request, 'apptwo/index.html')


def users(request):

    form = NewUserForm()

    # if request is post 
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request) # got ot index method 
        else:
            print("Error! Form Invalid")
            
    return render(request, 'apptwo/users.html', {'form': form})


