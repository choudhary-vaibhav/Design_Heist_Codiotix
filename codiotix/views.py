from pickle import FALSE
import os
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.shortcuts import redirect, render ,get_object_or_404
from django.db.models import Q
from .models import Tag , Cast , Genre ,Language , Movie , Webserie , Episode , Documentary
from django.contrib.auth.models import User
from django.http import FileResponse
def Home(request):
    languages = Language.objects.all()
    movie = 'movie'
    webserie = 'webserie'
    documentary = 'documentary'
    view = 'View More'
    context={
        'languages':languages,
        'movie':movie,
        'webserie':webserie,
        'documentary':documentary,
        'view':view
    }
    return render(request , 'codiotix/index.html' , context)


def SignItUp(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    else:
        if request.method =="POST":
            username = request.POST['username']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            if pass1 == pass2:
                if User.objects.filter(email = email).exists():
                    messages.error(request , 'Email you entered is already exists')
                    if len(pass1) < 8:
                        messages.error(request , 'Password must be equal or greater than 8 characters')
                    return redirect('Signup')
                else:
                    user = User(username = username , email = email)
                    user.set_password(pass1)
                    user.save()
                    messages.success(request , 'Account created successfully')
                    return redirect('Login')
            
            else:
                messages.error(request , 'Password not matching')
                return redirect('Signup')
        return render(request , 'codiotix/signup.html')

def LogItUp(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    else:
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username , password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request , 'Invalid Credentials')
                return redirect('Login')
            
        return render(request , 'codiotix/signin.html')


def LogItOut(request):
    logout(request)
    return redirect('home')




def ShowIt(request , pk):
    movies = ""
    webseries = ""
    documentaries = ""
    error = ""
    languages = ""
    lname = ""
    if pk == 'movie':
        movies = Movie.objects.all()
        if not movies:
            error = 'No movies are there in the platform....Soon we will add the movies'

    if pk == 'webserie':
        webseries = Webserie.objects.all()
        if not webseries:
            error = 'No webseries are there in the platform....Soon we will add the webseries'

    if pk == 'documentary':
        documentaries = Documentary.objects.all()
        if not documentaries:
            error = 'No documentaries are there in the platform....Soon we will add the documentaries'

    if pk == "View More":
        languages = Language.objects.all()
        lname = "Languages"
    
    context={
        'movies':movies,
        'webseries':webseries,
        'documentaries':documentaries,
        'error':error,
        'data':pk,
        'languages':languages,
        'lname':lname,
    }

    return render(request , 'codiotix/shows.html', context)


def ShowMovie(request , pk):
    movie = Movie.objects.get(id=pk)
    casts = movie.cast.all()
    context={
        'movie':movie,
        'casts':casts
    }
    return render(request , 'codiotix/movie.html' , context)

def ShowWebserie(request , pk):
    webserie = Webserie.objects.get(id=pk)
    webcasts = webserie.cast.all()
    episodes = Episode.objects.filter(webserie = webserie)
    context={
        'webserie':webserie,
        'episodes':episodes,
        'webcasts':webcasts
    }
    return render(request , 'codiotix/movie.html' , context)

def ShowDocumentary(request , pk):
    documentary = Documentary.objects.get(id=pk)
    casts = documentary.cast.all()
    context={
        'documentary':documentary,
        'casts':casts
    }
    return render(request , 'codiotix/movie.html' , context)

def ShowActor(request , pk):
    actor = Cast.objects.get(id=pk)
    context = {
        'actor':actor
    }
    return render(request , 'codiotix/movie.html' , context)




def Find(request):
     
    genres = Genre.objects.all()
    languages = Language.objects.all()

    context ={
        'genres':genres,
        'languages':languages,
    }

    return render(request , 'codiotix/search.html' , context)

def SearchResult(request):
    noshow = FALSE
    query = request.GET.get('query')
    res = ""
    error = ""
    notfound = ""
    movies = {}
    webseries = {}
    documentaries = {}
    if query:
        res = "Your Search Result"
        if len(query) > 40:
            error = query
        else:
            movies = Movie.objects.filter(Q(name__icontains = query) | Q(cast__name__icontains = query)| Q(tags__text__icontains = query)).distinct()
            webseries = Webserie.objects.filter(Q(name__icontains = query)| Q(tags__text__icontains = query) | Q(cast__name__icontains = query)).distinct()
            documentaries = Documentary.objects.filter(Q(name__icontains = query)| Q(tags__text__icontains = query) | Q(cast__name__icontains = query)).distinct()
            if not movies:
                if not webseries:
                    if not documentaries:
                        notfound = "No such Webseries , Movie  or Documentary available"
                
                    else:
                        noshow = True
                
                else:
                    noshow = True
            
            else:
                noshow = True


    context = {
        'movies':movies,
        'webseries':webseries,
        'documentaries':documentaries,
        'error':error,
        'notfound':notfound,
        'res':res,
        'noshow':noshow
    }
    return render(request , 'codiotix/result.html' ,context)


def SearchGenre(request , pk):
    gen = Genre.objects.get(id=pk)
    nogenre = ""
    movies = Movie.objects.all().filter(genre=gen).distinct()
    webseries = Webserie.objects.all().filter(genre=gen).distinct()
    documentaries = Documentary.objects.all().filter(genre=gen).distinct()
    if not movies:
        if not webseries:
            if not documentaries:
                nogenre = "Soon we will add movies , webseries and documentaries of such genre"

    context = {
        'movies':movies,
        'webseries':webseries,
        'documentaries':documentaries,
        'gen':gen,
        'nogenre':nogenre,
    }

    return render(request , 'codiotix/result.html' , context)


def SearchLanguage(request , pk):
    language = Language.objects.get(id=pk)
    noresult = ""
    movies = Movie.objects.filter(language = language).distinct()
    webseries = Webserie.objects.filter(language = language).distinct()
    documentaries = Documentary.objects.filter(language = language).distinct()
    print(movies)
    print(webseries)
    if not movies:
        if not webseries:
            noresult = "Soon we will add movies , webseries and documentaries of such language"
    context = {
        'movies':movies,
        'webseries':webseries,
        'documentaries':documentaries,
        'language':language,
        'noresult':noresult,
    }

    return render(request , 'codiotix/result.html' , context)

