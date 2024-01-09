from django.shortcuts import render, redirect
from posts.forms import postForm
from posts.models import Post

# Create your views here.
def add_post(request):
    if request.method == "POST":
        form = postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_posts")
    else:
        form = postForm()
    return render(request, "posts/add_post.html", {"form":form})


def edit_post(request, id):
    post = Post.objects.get(pk=id)
    # print(post.title)
    form = postForm(instance=post)

    if request.method == "POST":
        form = postForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    # else:
    #     form = postForm()
    return render(request, "posts/add_post.html", {"form":form})

def delete_post(request, id):
    post = Post.objects.get(pk = id)
    post.delete()
    return redirect("home")