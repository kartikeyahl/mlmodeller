from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('classification/', include('classification.urls')),
    path('deeplearning/', include('deeplearning.urls')),
    path('regression/', include('regression.urls')),
]
