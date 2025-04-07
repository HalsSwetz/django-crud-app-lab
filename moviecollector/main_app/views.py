from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Movie
from .forms import CriticForm

# Create your views here.



class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')

@login_required
def movie_index(request):
    movies = Movie.objects.filter(user=request.user)
    return render(request, 'movies/index.html', {'movies': movies})

@login_required
def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    critic_form = CriticForm()
    return render(request, 'movies/detail.html', {
        'movie': movie, 'critic_form': critic_form
    })

@login_required
def add_critic(request, movie_id):
    form = CriticForm(request.POST)
    if form.is_valid():
        new_critic = form.save(commit=False)
        new_critic.movie_id = movie_id
        new_critic.save()
    return redirect('movie-detail', movie_id=movie_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movie-index')
        else:
            error_message = 'Invalid sign up - try again'
            
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['name', 'genre', 'description', 'director', 'year']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ['genre', 'description', 'director', 'year']

class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = '/movies/'
