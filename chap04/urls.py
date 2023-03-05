from django.urls import path
# from myapp.views import my view

urlpatterns = [
    path('about/', MyView.as_view()),
    path('about/', AboutView.as_view())
]
