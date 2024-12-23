from django.contrib import admin
from django.shortcuts import render ,redirect
from django.urls import path, include
from django.views.generic import TemplateView

def Index(request):
    template_name='index.html'
    context = {
        'homePage':True,
        'title':'ML MODELLDER | Home'
    }
    return render(request, template_name,context)

def About(request):
    template_name='about us.html'
    context = {
        'aboutusPage':True,
        'title':'ML MODELLDER | About Us'
    }
    return render(request, template_name,context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index),
    path('about-us/',About),
    path('classification/', include('classification.urls')),
    path('blog/', include('blog.urls')),
    #path('deeplearning/', include('deeplearning.urls')),
    path('regression/', include('regression.urls')),
]
