from django.shortcuts import render
from django.contrib.auth.models import User
from blog.models import Comment, Post
from blog.forms import CommentForm

# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    # if request.method == 'POST':
        # posts = Post.objects.filter(title__trigram__similar="", body__trigram__similar="")
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if len(form.cleaned_data["body"]) > 2000:
                context["comment_body_error"] = "Comment cannot exceed 2000 characters."
            else:
                comment = Comment(
                    author= str(request.user.username),
                    body=form.cleaned_data["body"],
                    post=post
                )
                comment.save()
        else:
            print("Invalid")
            comment_body = request.POST.get("body")
            print(comment_body)
            if comment_body is None:
                context["comment_body_error"] = "Comment cannot be empty."
            else:
                if len(comment_body) == 0:
                    context["comment_body_error"] = "Comment cannot be empty."
                if len(comment_body) > 2000:
                    context["comment_body_error"] = "Comment cannot exceed 2000 characters."

    return render(request, "blog_detail.html", context)