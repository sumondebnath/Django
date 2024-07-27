from django import forms
from bulk_concept.models import Voulentears



class VoulentearsBulkForm(forms.ModelForm):
    class Meta:
        model = Voulentears
        fields = "__all__"



VoulentearsFormSet = forms.modelformset_factory(Voulentears, form=VoulentearsBulkForm, extra=15)