from typing import Any
from django.shortcuts import render, redirect
from posts.forms import postForm, CommentForm
from posts.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

#class based views--->

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

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

# add post class views.
@method_decorator(login_required, name="dispatch")
class addPostClassView(CreateView):
    model = Post
    form_class = postForm
    template_name = "posts/add_post.html"
    success_url = reverse_lazy("add_posts")
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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

@method_decorator(login_required, name="dispatch")
class EditPostView(UpdateView):
    model = Post
    form_class = postForm
    template_name = "posts/add_post.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("profile")

@login_required
def delete_post(request, id):
    post = Post.objects.get(pk = id)
    post.delete()
    return redirect("home")

@method_decorator(login_required, name="dispatch")
class DeletePostView(DeleteView):
    model = Post
    template_name = "posts/delete.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("profile")


class detailsView(DetailView):
    model = Post
    pk_url_kwarg = "id"
    template_name = "posts/ditailsview.html"

    def post(self, request, *args, **kwargs):
        comment_form =  CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all() # type: ignore
        comment_form = CommentForm()
        
        context["comments"] = comments
        context["comment_form"] = comment_form
        return context
