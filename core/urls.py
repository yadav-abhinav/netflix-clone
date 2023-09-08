from django.urls import path
from core import views
# from allauth

app_name='core'

urlpatterns = [
    path('',views.Home.as_view()),
    path('profile/',views.ProfileList.as_view(),name='profile_list'),
    path('profile/create/',views.ProfileCreate.as_view(),name='profile_create'),
    path('profile/<str:profile_id>/',views.WatchList.as_view(),name='watch_list'),
    path('movie/details/<str:movie_id>/',views.MovieDetails.as_view(),name='movie_details'),
    path('movie/play/<str:movie_id>/',views.PlayMovie.as_view(),name='play_movie'),
]