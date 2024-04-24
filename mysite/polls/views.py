from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import Question, Choice

def index(request):
    latest_quetion_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_quetion_list}
    return render(request, "polls/index.html", context)

def owner(request):
       return HttpResponse("Hello, world. 6ad2e2b2 8180fe9e is the polls index.")

def Detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not excist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def Results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def Vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
         selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
         #redisplay the question voting form.
        return render(request, "polls/detail.html",
                      {
                           "question": question,
                           "error_message": "Your didn't select a choice.",
                      },
                )
    else:
         selected_choice.votes += 1
         selected_choice.save()
         #always return an HttpResponseRedirect after successfully dealing
         #with a POST data. This prevents data from being posted twice if a
         #user hits the back button.
         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
