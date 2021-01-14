from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('update/<int:id>', UpdateView.as_view(), name='update'),
    path('delete/<int:id>', delete, name='delete'),
]