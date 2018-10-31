from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from .models import Question
from django.template import loader
from django.shortcuts import render


def index(request):
    least_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'least_question_list': least_question_list
    }
    print("查询到的查询集为：%s" % context)
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def redirect(request):
    return HttpResponseRedirect("/polls/json")


def return_json(request):
    return JsonResponse({"time": "morning"})


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist!")
    return render(request, 'polls/detail.html', {'question': 'question'})

