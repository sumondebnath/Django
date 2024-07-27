from django.shortcuts import render, redirect
from content.models import Content
from content.forms import ContentForm

from django.core.paginator import Paginator, PageNotAnInteger
from django.conf import settings

from django.db.models import Q

# Create your views here.

def AllContent(request):
    allCont = Content.objects.all()
    return render(request, "content/allContent.html", {"allContent":allCont})


def ContentList(request):
    contents = Content.objects.select_related("creator").all()
    print(contents.query)
    return render(request, "content/content_list.html", {"contents":contents})




def getContent(request, id):
    cont = Content.objects.get(id = id)
    template_name = "content/details.html"
    dictionary = {"cont":cont}
    return render(request, template_name, dictionary)

def getContentForeign(request, id):
    contents = Content.objects.select_related("creator").all().filter(id=id)
    return render(request, "content/get_content_foreign.html", {"contents":contents[0]})




def deleteContent(request, id):
    deleteCont = Content.objects.get(id = id).delete()
    # if request.method == "POST":
    #     deleteCont.delete()
    return redirect("all_content")
    # return render(request, "content/allContent.html", {"deleteCont": deleteCont})





def EditContent(request, id):
    content = Content.objects.get(id = id)
    form = ContentForm(instance=content)
    if request.method == "POST":
        form = ContentForm(request.POST, instance=content)
        if form.is_valid():
            form.save()
            return redirect("all_content")
    else:
        form = ContentForm(instance=content)
        
    return render(request, "content/edit_content_form.html", {"form":form})


def EditContentForeign(request, id):
    # content = Content.objects.get(id = id)
    content = Content.objects.select_related('creator').all().filter(id = id)
    for cont in content:
        form = ContentForm(instance=cont)
    if request.method == "POST":
        form = ContentForm(request.POST, instance=cont)
        if form.is_valid():
            form.save()
            return redirect("content_list")
    else:
        form = ContentForm(instance=cont)
        
    return render(request, "content/edit_content_foreign.html", {"form":form})




def insertContent(request):
    form = ContentForm()
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_content")
        
    return render(request, "content/insert_content_form.html", {"form":form})




def Content_Pagination(request):
    page_size = int(request.GET.get("page_size", getattr(settings, "PAGE_SIZE", 3)))
    page = request.GET.get("page", 1)

    # contents = Content.objects.all()

    search_query = request.GET.get("search", "")

    contents = Content.objects.filter(
        Q(id__icontains=search_query) | Q(name__icontains=search_query) | Q(title__icontains=search_query) | Q(content_type__icontains=search_query)
    )


    paginator = Paginator(contents, page_size)

    try:
        content_pages = paginator.page(page)
    except PageNotAnInteger:
        content_page = paginator.page(1)
    return render(request, "content/paginations.html", {"content_pages" : content_pages, "page_size" : page_size, "search_query": search_query})