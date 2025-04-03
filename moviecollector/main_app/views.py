from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Movie
from .forms import CriticForm

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def movie_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    critic_form = CriticForm()
    return render(request, 'movies/detail.html', {
        'movie': movie, 'critic_form': critic_form
    })

def add_critic(request, movie_id):
    form = CriticForm(request.POST)
    if form.is_valid():
        new_critic = form.save(commit=False)
        new_critic.movie_id = movie_id
        new_critic.save()
    return redirect('movie-detail', movie_id=movie_id)

class MovieCreate(CreateView):
    model = Movie
    fields = '__all__'

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['genre', 'description', 'director', 'year']

class MovieDelete(DeleteView):
    model = Movie
    success_url = '/movies/'
