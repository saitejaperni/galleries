from django.urls import path
from . import views
from .views import homepage, albumdetailview
urlpatterns = [
 path('home',homepage.as_view(), name='home'),
 path('albums', views.albumslist, name='albums'),
 path('actress', views.actresslist, name='actress'),
 path('actress/<slug:slug>/<int:id>', views.actressalbum, name='actressalbums'),
 path('albums/<int:id>', albumdetailview.as_view(), name='albumsdetail'),
 path('caro', views.carousel,name='caro')
]



