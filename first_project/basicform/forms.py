from django import forms 

class DateInput(forms.DateInput):
    input_type = 'date' 


class FormName(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Please enter name here"}), label='Name')    
    email = forms.EmailField(initial='example@mail.com', help_text='A valid email address, please.')  
    text =   forms.CharField(widget=forms.Textarea(attrs={'rows':'5'}), required=False) 
    Status = forms.BooleanField() # checkbox 
    city = forms.ChoiceField(label='City', choices=[
        ('', "Select Your City"),
        ('Barishal', "Barisal"),
        ('Chittagong', "Chittagong"),
        ('Dhaka', "Dhaka"),
        ('Khulna', "Khulna"), 
        ('Mymensingh', "Mymensingh"),
        ('Rajshahi', "Rajshahi"),
        ('Rangpur', "Rangpur"),
        ('Sylhet', "Sylhet")
    ])  
    typedChoice = forms.TypedChoiceField(choices=[
        ('', "Select Your City"),
        ('Barishal', "Barisal"),
        ('Chittagong', "Chittagong"),
        ('Dhaka', "Dhaka"),
        ('Khulna', "Khulna"), 
        ('Mymensingh', "Mymensingh"),
        ('Rajshahi', "Rajshahi"),
        ('Rangpur', "Rangpur"),
        ('Sylhet', "Sylhet")
    ], coerce=str)
    date = forms.DateField(widget=DateInput) 
    dateTime = forms.DateTimeField()  
    price = forms.DecimalField() 
    duration = forms.DurationField()
    Image = forms.FileField()
    ip = forms.GenericIPAddressField()
    time = forms.TimeField()
    website = forms.URLField() 
    slug = forms.SlugField()   