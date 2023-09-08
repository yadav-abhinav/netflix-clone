from django import views
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.models import Movie, Profile
from core.forms import ProfileForm

# Create your views here.
class Home(View):
    def get(self,request,*args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('core:profile_list')
        return render(request,'index.html')

@method_decorator(login_required,name='dispatch')
class ProfileList(View):
    def get(self,request,*args, **kwargs):
        profiles=request.user.profiles.all()
        return render(request,'profileList.html', { 'profiles':profiles })

@method_decorator(login_required,name='dispatch')
class ProfileCreate(View):
    def get(self,request,*args, **kwargs):
        form=ProfileForm()
        return render(request,'profileCreate.html', { 'form':form })

    def post(self,request,*args, **kwargs):
        form=ProfileForm(request.POST or None)
        print(request.POST.get('age_limit'))
        print(form.errors)
        if form.is_valid():
            print(form.cleaned_data)
            profile=Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect('core:profile_list')
        return render(request,'profileCreate.html', { 'form':form })

@method_decorator(login_required,name='dispatch')
class WatchList(View):
    def get(self,request,profile_id,*args, **kwargs):
        try:
            profile=Profile.objects.get(uuid=profile_id)
            movies=Movie.objects.all()
            if profile not in request.user.profiles.all():
                redirect(request,'core:profile_list')
            return render(request,'movieList.html',
            { 
                'movies':movies,
                'profile_name':profile.name
            })
        except Profile.DoesNotExist:
            return render(request,'core:profile_list')

@method_decorator(login_required,name='dispatch')
class MovieDetails(View):
    def get(self,request,movie_id,*args, **kwargs):
        try:
            movie=Movie.objects.get(uuid=movie_id)
            # if movie not in request:
            return render(request,'movieDetail.html',{ 'movie': movie })
        except Movie.DoesNotExist:
            return render(request,'core:watch_list')

@method_decorator(login_required,name='dispatch')
class PlayMovie(View):
    def get(self,request,movie_id,*args, **kwargs):
        try:
            movie=Movie.objects.get(uuid=movie_id)
            videos=movie.videos.values()
            return render(request,'showMovie.html',{ 'videos' : videos })
        except:
            return render(request,'core:watch_list')


