from django.urls import path
from django.shortcuts import render
from .views import ANNSigmoiod , ANNSoftmax

def Index(request):
    template_name="Deep Learning/Deep Learning.html"
    context = {
        "deeplearningPage":True
    }
    return render(request, template_name,context)


urlpatterns = [
    path('',Index,name="Deeplearning"),
    path('ann-sigmoid/',ANNSigmoiod),
    path('ann-softmax/',ANNSoftmax),
]