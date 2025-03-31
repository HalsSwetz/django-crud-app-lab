from django.shortcuts import render


# Create your views here.

class Movie:
    def __init__(self, name, genre, description, director, year):
        self.name = name
        self.genre = genre
        self.description = description
        self.director = director
        self.year = year

movies = [
    Movie('Groundhog Day', 'comedy', 'The same day over and over', 'Harold Ramis', 1993),
    Movie('Shaun of the Dead', 'comedy', 'Zombies are coming', 'Edgar Wright', 2004),
    Movie('Bridesmaids', 'comedy', 'Maid of honor is a mess', 'Paul Feig', 2011),
    Movie('Superbad', 'comedy', 'Two high school seniors want to have the best night ever', 'Greg Mottola', 2007),
    Movie('Men in Black', 'sci-fi', 'Two agents work for a unofficial government agency', 'Barry Sonnenfield', 1997),
    Movie('The Departed', 'drama', 'A South Boston cop goes undercover', 'Martin Scorcese', 2006),
]

def movie_index(request):
    return render(request, 'movies/index.html', {'movies': movies})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')