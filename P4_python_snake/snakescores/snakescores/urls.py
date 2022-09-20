"""snakescores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
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