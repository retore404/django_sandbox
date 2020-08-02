from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import SignUpForm, VoteForm
from .models import Choice, Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'signup/index.html', context)

def detail(request, question_id):
    user = request.user
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = VoteForm(request.POST, question=question)
        if form.is_valid():
            form.save()
            return redirect('signup:results', question_id=question.id)
    else:
        form = VoteForm(question=question)

    context = {'user':user, 'question':question, 'form':form}
    return render(request, "signup/detail.html", context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'signup/results.html', {'question': question})

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'signup/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('signup:results', args=(question.id,)))

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup:index')
    else:
        form = SignUpForm()

    context = {'form':form}
    return render(request, 'signup/signup.html', context)