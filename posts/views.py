from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post
from posts.forms import PostForm

def posts_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', context={'posts': posts})


def post_detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post_detail.html', context={'post': post})


class PostCreateView(View):

    def get(self, request):
        form = PostForm()
        return render(request, 'posts/post_create.html', context={'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(post)
        return render(request, 'posts/post_create.html', context={'form': form})
