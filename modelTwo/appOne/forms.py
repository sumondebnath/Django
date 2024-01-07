from django import forms
from appOne.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"
        # fields = ["name", "roll"]
        # exclude = ["roll"]
        labels = {
            "name" : "Student Name",
            "roll" : "Student Roll",
        }
        widgets = {
            "name" : forms.TextInput(attrs={"placeholder":"Enter Your Full Name "}),
        }
        help_texts = {
            "address" : "Write your full address.",
        }
        error_messages = {
            "name" : {"required":"must be your name is required."},
        }