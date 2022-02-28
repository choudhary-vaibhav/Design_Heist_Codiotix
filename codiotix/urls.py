from django.urls import path
from . import views

urlpatterns = [
      path('' , views.Home , name="home"),
      path('signup/' , views.SignItUp , name="Signup"),
      path('login/' , views.LogItUp , name="Login"),
      path('logout/' , views.LogItOut , name="Logout"),
      path('show/<str:pk>' , views.ShowIt , name="ShowIt"),
      path('find/' , views.Find , name="find"),
      path('Movies/<str:pk>/The_Codiotix' , views.ShowMovie , name="ShowMovie"),
      path('Webseries/<str:pk>/The_Codiotix' , views.ShowWebserie , name="ShowWebserie"),
      path('Documentaries/<str:pk>/The_Codiotix' , views.ShowDocumentary , name="ShowDocumentary"),
      path('Genre/<str:pk>/The_Codiotix' , views.SearchGenre , name="SearchGenre"),
      path('Language/<str:pk>/The_Codiotix' , views.SearchLanguage , name="SearchLanguage"),
      path('Actor/<str:pk>/The_Codiotix' , views.ShowActor , name="ShowActor"),
      path('searchresults/' , views.SearchResult , name="SearchResult"),
]