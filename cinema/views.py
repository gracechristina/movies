from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post, PostAd, Movie
from .forms import BookingForm,PostForm, MovieForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

def movie_new(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'cinema/movie_new.html', {'form': form})

def movie_detail(request,pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request,'cinema/movie_detail.html',{'movie': movie})

def post_list(request):
    posts = Post.objects.filter().order_by('published_date')
    return render(request, 'cinema/post_list.html', {'post': post})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'cinema/post_detail.html',{'post':post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'cinema/post_edit.html', {'form': form})


@login_required
def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm(instance=post)
    return render(request, 'cinema/post_edit.html',{'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'cinema/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def booking(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, 'cinema/name.html', {'form': form})
