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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index),
    path('classification/', include('classification.urls')),
    path('deeplearning/', include('deeplearning.urls')),
    path('regression/', include('regression.urls')),
]
