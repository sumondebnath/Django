from django.shortcuts import render, redirect
from posts.forms import postForm
from posts.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_post(request):
    if request.method == "POST":
        form = postForm(request.POST)
        if form.is_valid():
            # form.cleaned_data["author"] = request.user   # not working
            form.instance.author = request.user     # this class ar object instance a user ke bosalam.
            form.save()
            return redirect("add_posts")
    else:
        form = postForm()
    return render(request, "posts/add_post.html", {"form":form})

@login_required
def edit_post(request, id):
    post = Post.objects.get(pk=id)
    # print(post.title)
    form = postForm(instance=post)

    if request.method == "POST":
        form = postForm(request.POST, instance=post)
        if form.is_valid():
            form.instance.author = request.user     # this class ar object instance a user ke bosalam.
            form.save()
            return redirect("home")
    # else:
    #     form = postForm()
    return render(request, "posts/add_post.html", {"form":form})

@login_required
def delete_post(request, id):
    post = Post.objects.get(pk = id)
    post.delete()
    return redirect("home")