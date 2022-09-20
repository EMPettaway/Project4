from django.shortcuts import render
from dataclasses import dataclass
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Scores
# Add the following import
from django.http import HttpResponse


class ScoresCreate(CreateView):
    model = Scores
    fields = '__all__'
    template_name = 'scores/score_form.html'
    success_url = '/scores/'

class ScoresUpdate(UpdateView):
  model = Scores
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['highscore']

class ScoresDelete(DeleteView):
  model = Scores
  success_url = '/scores/'

# class Scores:
#     def __init__(self, username, highscore):
#         self.username = username
#         self.highscore = highscore

# highscores = [
#     Scores('ChaseDope', 11),
#     Scores('EMP', 6),
#     Scores('Jo', 8),
# ]

# Define the home view
def home(request):
  return HttpResponse('<h1>Snake by EP (Project 4)</h1>')

def about(request):
    return render(request, 'about.html')

def scores_index(request):
    highscores = Scores.objects.all()
    return render(request, 'scores/index.html', { 'highscores': highscores})

def scores_detail(request, scores_id):
    highscore = Scores.objects.get(id=scores_id)
    return render(request, 'scores/detail.html', {'highscore': highscore })

def howto(request):
    return render(request, 'howto.html')

def startgame(request):
    return render(request, 'startgame.html')

def score_update(request, scores_id):
    highscore = Scores.objects.filter(id=scores_id).update()

def score_delete(request, scores_id):
    highscore = Scores.objects.filter(id=scores_id).delete()