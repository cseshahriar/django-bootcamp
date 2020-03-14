from django import forms
from apptwo.models import User

# user model form  
class NewUserForm(forms.ModelForm):
    # custom validation 
    class Meta():
        model = User
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'email')  