from django import forms

class contactForm(forms.Form):

    # image = forms.ImageField()

    file = forms.FileField()

    name = forms.CharField(label="UserName")
    email = forms.EmailField(label="UserEmail")
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    date = forms.DateField()
    dateTime = forms.DateTimeField()
    check = forms.BooleanField()

    CHOICES = [(1, "ONE"), (2, "TWO"), (3, "THREE"), (4, "FOUR"), (5, "FIVE")]
    rating = forms.ChoiceField(choices = CHOICES)

    seclects = forms.MultipleChoiceField(choices = CHOICES)