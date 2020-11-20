from django.urls import path
from django.shortcuts import render
from django.views.generic import TemplateView
from .views import DecisionTree, KNearestNeighbors, KernelSVM, LogisticRegression, NaiveBayes, RandomForest, SupportVector

def Index(request):
    template_name="Classification/Classification.html"
    context = {
        "classificationPage":True
    }
    return render(request, template_name,context)

urlpatterns = [
    path('',Index,name="classfication"),
    path('decision-tree/', DecisionTree),
    path('k-nearest-neighbors/', KNearestNeighbors),
    path('kernel-svm/', KernelSVM),
    path('logistic-regression/', LogisticRegression),
    path('naive-bayes/', NaiveBayes),
    path('random-forest/', RandomForest),
    path('support-vector/', SupportVector)
]
