from django.urls import path
from . import views

urlpatterns = [
    path('', views.classify_text_view, name='classify_text'),
]
