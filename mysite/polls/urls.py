from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex /polls/
    path("", views.index, name="index"),
    path('owner', views.owner, name='owner'),
    # ex: /polls/5/
    path("<int:question_id>/", views.Detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.Results, name ="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.Vote, name="vote"),
]
