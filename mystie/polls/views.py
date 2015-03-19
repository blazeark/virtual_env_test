from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse, Http404, HttpResponseRedirect
from polls.models import Question,Choice
from django.template import loader, RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name =  'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'












#def index(request):
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = RequestContext(request, {'latest_question_list': latest_question_list})
#    return HttpResponse(template.render(context))

#def detail(request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exsist")
#    return HttpResponse("Question %s" % question_id)

#def results(request, question_id):
#    return render(request, 'polls/results.html', {'question': get_object_or_404(Question,pk=question_id)})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question': p,'error_message':"nope.",})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

