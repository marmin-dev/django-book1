from django.urls import path

from . import views

urlpatterns = [
    path('articles/2003/', views.special_case2003),
    path('articles/<int:year>', views.year_archive)
]
