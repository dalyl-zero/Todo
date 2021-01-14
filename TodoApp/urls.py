from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='app'),
    path('update/<int:id>', UpdateView.as_view(), name='update')
]