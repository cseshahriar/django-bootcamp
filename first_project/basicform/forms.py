from django import forms 
from django.core import validators


class DateInput(forms.DateInput): 
    input_type = 'date' 


class FormName(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Please enter name here"}), label='Name', required=False)     
    email = forms.EmailField(initial='example@mail.com', help_text='A valid email address, please.')  
    text =   forms.CharField(widget=forms.Textarea(attrs={'rows':'5'}), required=False) 
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
 
    # form validation 
    '''
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('GOTCHA BOT!')
        return botcatcher
    '''

    def clean(self):
        all_clean_data = super().clean()  
        email = all_clean_data['email']
        name = all_clean_data['name'] 

        if(len(name) <= 0):
            raise forms.ValidationError('Name field is required!') 