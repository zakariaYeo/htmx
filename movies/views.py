from django.forms import models
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from movies.models import Movies
from movies.forms import MoviesForm
from django.contrib import messages



# Create your views here.

class IndexView(ListView):
    model = Movies
    template_name = 'movies/index.html'
    context_object_name = 'films'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Films"
        return context


def check_name(request):
    name = request.POST.get('name')

    if Movies.objects.filter(name__iexact=name).exists():
        return HttpResponse("<div id='name-error' class='text-danger'>Ce film est déjà enregistré.</div>")
    else:
        return HttpResponse("<div id='name-error' class='text-success'>Vous pouvez l'enregistrer.</div>")

def add_film(request):
    name = request.POST.get('name')

    if Movies.objects.filter(name__iexact=name).exists():
        messages.ERROR(request, f'{name} existe déjà.')
    else:
        film = Movies.objects.create(name=name)
    films = Movies.objects.all()
    # request.user.film.add(film)    

    context = {
        'films': films,

    }
    return render(request, 'movies/partials/films_list.html', context)

def delete_film(request, pk):
    try:
        movie = get_object_or_404(Movies, pk=pk)
        movie.delete()
        films = Movies.objects.all()
        return render(request, 'movies/partials/films_list.html', {'films':films})
    except:
        messages.error(request, 'Un problème est survenu.')

def search_film(request):
    search_text = request.POST.get('search')

    results = Movies.objects.filter(name__icontains=search_text)
    context = {
        'results': results,
    }

    return render(request, 'movies/partials/search_results.html', context)
