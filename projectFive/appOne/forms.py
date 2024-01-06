from django import forms
from django.core import validators

class contactForm(forms.Form):

    # image = forms.ImageField()

    file = forms.FileField(required=False)

    name = forms.CharField(label="UserName :", help_text="Total length must be within 80 charecters.", widget=forms.TextInput(attrs={"placeholder":"Enter Your Full Name: "}))
    email = forms.EmailField(label="UserEmail")
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    date = forms.DateField(widget=forms.DateInput(attrs={"type":"Date"}))
    dateTime = forms.DateTimeField(widget=forms.DateInput(attrs={"type":"datetime-local"}))
    check = forms.BooleanField()

    CHOICES = [(1, "ONE"), (2, "TWO"), (3, "THREE"), (4, "FOUR"), (5, "FIVE")]
    rating = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect)

    seclects = forms.MultipleChoiceField(choices = CHOICES, widget=forms.CheckboxSelectMultiple)

    message = forms.CharField(widget=forms.Textarea)

# class LoginForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.EmailField(widget=forms.EmailInput)

    # def clean_name(self):
    #     valName = self.cleaned_data["name"]
    #     if len(valName) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 charecters.")
    #     return valName
    # def clean_email(self):
    #     valMail = self.cleaned_data["email"]
    #     if "@" not in valMail or ".com" not in valMail:
    #         raise forms.ValidationError("Incorrect Email.")
    #     return valMail

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valName = self.cleaned_data["name"]
    #     valMail = self.cleaned_data["email"]
    #     if len(valName) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 charecters.")
    #     if "@" not in valMail or ".com" not in valMail:
    #         raise forms.ValidationError("Incorrect Email.")
        

def lengthCheck(value):
    if len(value) < 10:
        raise forms.ValidationError("Type some more texts.") 

class LoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message="Ensure this value has at least 10 characters.")])
    email = forms.EmailField(widget=forms.EmailInput, validators=[validators.EmailValidator])
    age = forms.IntegerField( validators=[validators.MinValueValidator(16), validators.MaxValueValidator(32)])
    file = forms.FileField(widget=forms.FileInput, validators=[validators.FileExtensionValidator(allowed_extensions=["pdf", "png"])])
    text = forms.CharField(widget=forms.Textarea, validators=[lengthCheck])




class passwordvalidationForms(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        passw = self.cleaned_data["password"]
        conf_pass = self.cleaned_data["confirm_password"]

        if passw != conf_pass:
            raise forms.ValidationError("Password donot match.")