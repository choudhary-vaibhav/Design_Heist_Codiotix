from asyncio.windows_events import NULL
from django.db import models

class Tag(models.Model):
    text = models.CharField(max_length = 40)

    def __str__(self):
        return self.text

class Cast(models.Model):
    name = models.CharField(max_length=50)
    actorImage = models.ImageField(upload_to = 'images/')
    about = models.TextField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    CHOICES = (
        ('Drama' , 'Drama'),
        ('Action and Adventure' , 'Action and Adventure'),
        ('Romance' , 'Romance'),
        ('Comedy' , 'Comedy'),
        ('Thriller' , 'Thriller'),
        ('Horror' , 'Horror')
    )

    type = models.CharField(max_length=50 , choices= CHOICES , unique = True)
    image = models.ImageField(upload_to = 'genreimg/' , default=NULL)

    def __str__(self):
        return self.type


class Language(models.Model):
    LANG = (
        ('Hindi' , 'Hindi'),
        ('English' , 'English'),
        ('Tamil' , 'Tamil'),
        ('Telegu' , 'Telegu'),
        ('Malayalam' , 'Malayalam'),
        ('Kannada' , 'Kannada'),
        ('Marathi' , 'Marathi'),
        ('Bengali' , 'Bengali'),
        ('Punjabi' , 'Punjabi'),
        ('Gujarati' , 'Gujarati'),
    )

    language_type = models.CharField(max_length=50 , choices= LANG , unique = True)
    image = models.ImageField(upload_to = 'languageimg/' , default=NULL)

    def __str__(self):
        return self.language_type




class Movie(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'movieimg/')
    video = models.FileField(upload_to = 'movies/')
    desc = models.TextField()
    tags = models.ManyToManyField(Tag)
    cast = models.ManyToManyField(Cast)
    genre = models.ForeignKey(Genre , on_delete = models.CASCADE)
    language = models.ForeignKey(Language , on_delete = models.CASCADE)

    def __str__(self):
        return self.name



class Webserie(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'webserieimg/')
    desc = models.TextField()
    tags = models.ManyToManyField(Tag)
    cast = models.ManyToManyField(Cast)
    genre = models.ForeignKey(Genre , on_delete = models.CASCADE)
    language = models.ForeignKey(Language , on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Documentary(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'movieimg/')
    video = models.FileField(upload_to = 'movies/')
    desc = models.TextField()
    tags = models.ManyToManyField(Tag)
    cast = models.ManyToManyField(Cast)
    genre = models.ForeignKey(Genre , on_delete = models.CASCADE)
    language = models.ForeignKey(Language , on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Episode(models.Model):
    episode_number = models.IntegerField()
    name = models.CharField(max_length = 100)
    video = models.FileField(upload_to = 'webserieepi/')
    webserie = models.ForeignKey(Webserie , on_delete = models. CASCADE)

    def __str__(self):
        return f"{self.webserie.name} - {self.name}"


    

