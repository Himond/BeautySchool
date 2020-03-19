from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView
from .models import Post, Comment, Postlike
from .forms import CommentForm, LikeForm
from django.db.models import Sum

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    postlike = Postlike.objects.filter(post_name=post).aggregate(total_likes=Sum('post_likes'))
    postlike_name = Postlike.objects.filter(post_name=post)
    try:
        post_name = postlike_name.get(name=request.user)
    except:
        post_name = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        like_form = LikeForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.name = request.user
            # Save the comment to the database
            new_comment.save()
        elif request.POST["post_likes"] == "1":
            if post_name == None:
                new_like = like_form.save(commit=False)
                new_like.post_name = post
                new_like.name = request.user
                new_like.post_likes = 1
                new_like.save()
        elif request.POST["post_likes"] == "-1":
            if post_name == None:
                new_like = like_form.save(commit=False)
                new_like.post_name = post
                new_like.name = request.user
                new_like.post_likes = -1
                new_like.save()
    else:
        comment_form = CommentForm()
        like_form = LikeForm()
    comments = post.comments.filter(active=True)
    postlike = Postlike.objects.filter(post_name=post).aggregate(total_likes=Sum('post_likes'))
    post_name = Postlike.objects.filter(post_name=post)
    try:
        post_name = post_name.get(name=request.user)
    except:
        post_name = None
    return render(request,
                  'blog/post/detail.html',
                 {'post': post,
                   'postlike': postlike,
                  'post_name': post_name,
                  'like_form':like_form,
                  'comments': comments,
                  'comment_form': comment_form})

