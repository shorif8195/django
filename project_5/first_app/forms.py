from django import forms 
from django.core import validators

# widgets - field to html input

class contactForm(forms.Form):
    name = forms.CharField(label="User Name",  help_text = "total length must be whithin 79 charecters",required=False,  widget= forms.Textarea(attrs= {'id':'text_area', 'class' :'class2','placeholder': 'Enter your name'}))
    # file = forms.FileField()


    email = forms.EmailField()
    age = forms.CharField(widget=forms.NumberInput)
    weight = forms.FloatField()
    check = forms.BooleanField()
    birthday = forms.DateField(widget= forms.DateInput(attrs={'type':'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))

    MEAL = [('P','Pepperoni'),('M','Mashroom'),('B','Beaf')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)

    CHOICE = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICE, widget= forms.RadioSelect)

# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     def clean_name(self):
#         valname = self.cleaned_data['name']
#         if len(valname) <10:
#             raise forms.ValidationError("Enter a name with at least 10 characters")
#         return valname
    
#     def clean_email(self):
#         valemail = self.cleaned_data['email']
#         if ('.com') not in valemail:
#             raise forms.ValidationError("enter a valied email")

class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10,message= 'minimum length should be 10 characters')])
    email = forms.CharField(validators= [validators.EmailValidator(message='enter a valied email brooh')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(35,message='maximum age should be 35'), validators.MinValueValidator(10,message='minimum age should be 10')])

    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png','jpg','jpeg'],message='file only pdf allowed')])


class passwordValidationProject(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(15)])
    password = forms.CharField(widget=forms.PasswordInput)
    c_password = forms.CharField(widget=forms.PasswordInput,label='Confirm password')

    def clean(self):
        cleaned_data= super().clean()

        val_pass = self.cleaned_data['password']
        val_conpass= self.cleaned_data['c_password']

        

        if val_conpass != val_pass:
            raise forms.ValidationError("password does not matched")
        
