from django.urls import path
from .views import DecisonTreeRegression, MultipleLinearRegression, PolynomialRegression, RandomForestRegression, SimpleLinearRegression, SupportVectorRegression

urlpatterns = [
    path('decisiontree-regression/', DecisonTreeRegression),
    path('multiple-linear-regression/', MultipleLinearRegression),
    path('polynomial-regression/', PolynomialRegression),
    path('random-forest-regression/', RandomForestRegression),
    path('simple-linear-regression/', SimpleLinearRegression),
    path('support-vector-regression/', SupportVectorRegression),
]
