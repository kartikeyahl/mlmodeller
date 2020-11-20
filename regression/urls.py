from django.urls import path
from django.shortcuts import render
from .views import DecisonTreeRegression, MultipleLinearRegression, PolynomialRegression, RandomForestRegression, SimpleLinearRegression, SupportVectorRegression


def Index(request):
    template_name="Regression/Regression.html"
    context = {
        "regressionPage":True
    }
    return render(request, template_name,context)
urlpatterns = [
    path('',Index,name="regression"),
    path('decisiontree-regression/', DecisonTreeRegression),
    path('multiple-linear-regression/', MultipleLinearRegression),
    path('polynomial-regression/', PolynomialRegression),
    path('random-forest-regression/', RandomForestRegression),
    path('simple-linear-regression/', SimpleLinearRegression),
    path('support-vector-regression/', SupportVectorRegression),
]
