from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone


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


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist!")
#     return render(request, 'polls/detail.html', {'question': question.question_text})

# def detail(request, question_id):
#     question_all = Question.objects.get(id=1)
#     print("反向链接为:", question_all.choice_set.all)
#     # print("所有的问题为：", [choice.choice_text for choice in question_all.choice_set.all])
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'least_question_list'

    def get_queryset(self):
        """
        return the last five published questions (not include those set to be published in the future)
        :return:
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
