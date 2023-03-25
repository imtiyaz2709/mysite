from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from django.http import HttpResponse
from .models import *


def index(r):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list
    }
    return render(r,"polls/index.html",context)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{"question":question})

def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/results.html', {"question":question})

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExit):
        return render(request, 'polls/detail.html',{
            "question":question,
            "error_message":"you did't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect(results,question_id)
    