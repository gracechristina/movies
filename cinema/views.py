from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post, PostAd, Movie, Theatre
from .forms import BookingForm,PostForm, MovieForm, TheatreForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

def movie_new(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'cinema/movie_new.html', {'form': form})

def theatre_new(request):
    if request.method == "POST":
        form = TheatreForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('movie_list')
    else:
        form = TheatreForm()
    return render(request, 'cinema/theatre_new.html', {'form': form})

def movie_detail(request,pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request,'cinema/movie_detail.html',{'movie': movie})

def movie_list(request):
    movies = Movie.objects.filter().order_by("title")
    return render(request,'cinema/movie_list.html', {'movies' : movies})

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
    movielist = Movie.objects.all().order_by('title')
    cinemalist = Theatre.objects.all().order_by('theatre_name')
    return render(request, 'cinema/booking.html', {'movielist': movielist, 'cinemalist':cinemalist})

def admin(request):
    return render(request, 'cinema/admin.html',{} )
