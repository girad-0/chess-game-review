from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("review/<int:review_id>/", views.review_page, name="review_page"),
]