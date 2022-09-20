from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('howto/', views.howto, name='howto'),
    path('startgame/', views.startgame, name='startgame'),
    path('scores/create/', views.ScoresCreate.as_view(), name='score_form'),
    path('scores/', views.scores_index, name='index'),
    path('scores/<int:scores_id>/', views.scores_detail, name='detail'),
    path('scores/<int:scores_id>/update/', views.ScoresUpdate.as_view(), name='score_update'),
    path('scores/<int:scores_id>/delete/', views.ScoresDelete.as_view(), name='score_delete'),
]