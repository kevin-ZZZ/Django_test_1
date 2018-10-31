from django.urls import path

from . import views

urlpatterns = [
    path(r'redirect', views.redirect, name='redirect'),
    path(r'json', views.return_json, name='json'),
    path(r'', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
