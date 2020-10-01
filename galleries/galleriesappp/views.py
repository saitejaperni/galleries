from django.shortcuts import render, get_object_or_404
from .models import Actress,Albums, carouselslide,carouselslideX
from django.views.generic import (
    TemplateView, DetailView, ListView
)
# Create your views here.
class homepage(TemplateView):
    template_name = 'homepage.html'

    # queryset = Article.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actres_albums'] = Albums.objects.all()
        context['actresslist'] = Actress.objects.all()
        context['carousellist'] = carouselslide.objects.all()
        context['carousellistX'] = carouselslideX.objects.all()
        return context

def albumslist(request):
   actres_albums = Albums.objects.all()
   return render(request, 'albumslist.html',{'album':actres_albums})

def actresslist(request):
   actres_list = Actress.objects.all()
   return render(request, 'actresslist.html',{'actres_list':actres_list})

def actressalbum(request,slug,id):
    albums_list= Albums.objects.filter(actress= id)
    #albums_list= Albums.objects.all()
    return render(request,'actressalbums.html',{'albums_list':albums_list})


class albumdetailview(DetailView):
    template_name = 'albumdetails.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Albums, id=id_)


def carousel(request):
    caurosel_list= carouselslide.objects.all()
    #albums_list= Albums.objects.all()
    return render(request,'carousel.html',{'caurosel_list':caurosel_list})