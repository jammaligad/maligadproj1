from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question
from .forms import QuestionModelForm

def index(request): 
    context = {}
    questions = Question.objects.all()
    context['questions'] = questions
    return render(request, 'index.html', context)

def help(request):
    return render(request, 'This is the help page.')

def detail(request, question_id):
    context = {}
    context['question'] = Question.objects.get(id=question_id)
    return render(request, 'detail.html', context)

def update(request, question_id):
    context = {}
    question = Question.objects.get(id=question_id)

    if request.method == 'POST':
        form = QuestionModelForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return HttpResponse('Question updated')
        else:
            context['form'] = form
            render(request, 'update.html', context)
    else:
        context['form'] = QuestionModelForm(instance=question)
    return render(request, 'update.html', context)