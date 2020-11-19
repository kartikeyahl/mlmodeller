from django.urls import path
from .views import DecisionTree, KNearestNeighbors, KernelSVM, LogisticRegression, NaiveBayes, RandomForest, SupportVector
urlpatterns = [
    path('decision-tree/', DecisionTree),
    path('k-nearest-neighbors/', KNearestNeighbors),
    path('kernel-svm/', KernelSVM),
    path('logistic-regression/', LogisticRegression),
    path('naive-bayes/', NaiveBayes),
    path('random-forest/', RandomForest),
    path('support-vector/', SupportVector)
]
