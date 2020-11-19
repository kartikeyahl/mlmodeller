from django.urls import path
from .views import ANNSigmoiod , ANNSoftmax
urlpatterns = [
    path('ann-sigmoid/',ANNSigmoiod),
    path('ann-softmax/',ANNSoftmax),
]