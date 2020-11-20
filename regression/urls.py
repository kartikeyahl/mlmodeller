from django.urls import path
from django.shortcuts import render
from .views import DecisonTreeRegression, MultipleLinearRegression, PolynomialRegression, RandomForestRegression, SimpleLinearRegression, SupportVectorRegression


def Index(request):
    template_name="Regression/Regression.html"
    context = {
        "regressionPage":True,
        'title':'ML MODELLDER | Regression',
    }
    return render(request, template_name,context)
urlpatterns = [
    path('',Index,name="regression"),
    path('decisiontree-regression/', DecisonTreeRegression,name="decisiontree-regression"),
    path('multiple-linear-regression/', MultipleLinearRegression,name="multiple-linear-regression"),
    path('polynomial-regression/', PolynomialRegression,name="polynomial-regression"),
    path('random-forest-regression/', RandomForestRegression,name="random-forest-regression"),
    path('simple-linear-regression/', SimpleLinearRegression,name="simple-linear-regression"),
    path('support-vector-regression/', SupportVectorRegression,name="support-vector-regression"),
]
