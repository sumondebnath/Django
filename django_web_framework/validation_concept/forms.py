
from django import forms
import re
from validation_concept.models import UserRegistration
from validation_concept.constants import GENDER

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = "__all__"

        widgets = {
            "password" : forms.PasswordInput(),
            "confirm_password" : forms.PasswordInput(),
            "gender": forms.Select(choices=GENDER),
            "date_of_birth" : forms.DateInput(attrs={"type": "date"}),
            "email" : forms.EmailInput(),
            "website_url" : forms.URLInput()
        }
    
        # Field Level validations
    def clean_phone_number(self):
        phoneNumber = self.cleaned_data.get("phone_number")
        if phoneNumber:
            pattern = re.compile(r"(01)?[3-9][0-9]{8}")
            if not re.fullmatch(pattern, phoneNumber):
                raise forms.ValidationError("Invalid Phone Number! Example: 018********")
            return phoneNumber
        

        # Forms level validations.
    def clean(self):
        cleaned_data = super().clean()

        input_password = cleaned_data.get("password")
        input_confirm_password = cleaned_data.get("confirm_password")
        input_username = cleaned_data.get("username")

        if input_password and input_confirm_password:
            if input_password != input_confirm_password:
                raise forms.ValidationError("Password and Confirm Password Does Not Matched!")
        
        if input_password and input_username:
            if input_password == input_username:
                raise forms.ValidationError("Username and Password Should Not be Matched!")
        
        return cleaned_data