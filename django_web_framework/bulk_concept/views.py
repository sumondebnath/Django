from django.shortcuts import render, redirect
from bulk_concept.models import Voulentears
from bulk_concept.forms import VoulentearsFormSet

# Create your views here.

def Voulentear_Bulk_insert(request):

    if request.method == "POST":
        formset = VoulentearsFormSet(request.POST, prefix="voulentear")
        if formset.is_valid():
            voulentears = formset.save(commit=False)
            Voulentears.objects.bulk_create(voulentears)
            return redirect("bulk_insert")
    else:
        formset = VoulentearsFormSet(queryset=Voulentears.objects.none(), prefix="voulentear")

    return render(request, "bulk_concept/bulk_insert.html", {"formset" : formset})

