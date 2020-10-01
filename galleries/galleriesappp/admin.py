from django.contrib import admin

# Register your models here.

from .models import Actress, Albums,carouselslide,carouselslideX


admin.site.register(Actress)
admin.site.register(Albums)
admin.site.register(carouselslide)
admin.site.register(carouselslideX)