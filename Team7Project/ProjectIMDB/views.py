from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Movie, Actor, Genre, Rating
from django.template import loader
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, OrderForm
from django.contrib import messages


# Create your views here.

def index(request):
    movie_list = Movie.objects.all()
    template = loader.get_template('index.html')
    top_movies = Movie.objects.all().order_by('-rating__movie')[:5]
    new_release = Movie.objects.all().order_by('-release_year')[:2]
    context = {
        'movie_list': movie_list,
        'top_movies': top_movies,
        'new_release': new_release,
    }
    return HttpResponse(template.render(context, request))


def about(request):
    return render(request, 'about.html')


def redirect_view(request):
    response = redirect('https://www.google.com/')
    return response


def movie_index(request):
    movies = Movie.objects.all()
    context_data = {
        'movies': movies,
    }

    return render(request, 'browse-movies.html', context_data)

#Register
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('/?ref_=nv_home')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = RegisterForm()

    return render(request, 'register.html', {"form": form})


class filter_objects(ListView):
    model = Movie
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Movie.objects.filter(
            Q(director__icontains=query) | Q(movie_title__icontains=query) | Q(genre__genre_title__icontains=query)
        ).distinct()
        return object_list


@login_required(login_url='/login')
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            msg = "Your order has been placed successfully!"
            form.save()
            newform = form()
            return render(request, 'order-movies.html', {'orderform': newform, 'msg': msg})

    else:
        form = OrderForm()
    return render(request, 'order-movies.html', {'form': form})
