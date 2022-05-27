from django.urls import path

from .views import BookAPIDetailView, BookAPIView

urlpatterns = [
    path("<int:pk>/", BookAPIDetailView.as_view()),
    path("", BookAPIView.as_view()),
]
